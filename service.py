import struct
import binascii
import json

from google.protobuf import text_format

from gevent import core
from gevent import socket
from gevent.hub import get_hub
from gevent.event import AsyncResult
from gevent.baseserver import BaseServer

from prototype import utils_pb2

from pb_to_dict import protobuf_to_dict

class BaseAsyncResult(AsyncResult):

    def __init__(self, response_class, *args, **kwargs):
        self.response_class = response_class
        super(BaseAsyncResult, self).__init__(*args, **kwargs)

    def set(self, value):
        response = self.response_class()
        response.ParseFromString(value)
        super(BaseAsyncResult, self).set(response)


class BaseChannel(object):

    def __init__(self, host=None, port=None, service=None):
        self.pending_response = {}
        self.host = host
        self.port = port
        self.hub = get_hub()
        self.loop = self.hub.loop
        self.message_buf = ''
        self.max_length = 5000
        self.header_length = struct.calcsize('!HBBH')
        self.socket = None
        self._idle_watcher = self.loop.idle()
        self._idle_watcher.start(self._update)

    def _get_connection(self):
        if self.socket == None:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.host, self.port))
            self.socket = sock
            self._read_watcher = self.loop.io(self.socket.fileno(), core.READ)
            self._read_watcher.start(self._do_read)
            self._write_watcher = self.loop.io(self.socket.fileno(), core.WRITE)
            self._write_watcher.start(self._do_write)
        return self.socket

    def _do_write(self):
        pass

    def _do_read(self):
        self.message_buf += self.socket.recv(self.max_length)
        while len(self.message_buf) >= self.header_length:
            self._do_handle()

    def _do_handle():
        pass

    def _update(self):
        """
            1, handle controller status change like cancel
            2, check connection status and reconnect(if neccessay)
        """
        pass

    def print_message(self, message, prefix='Message:'):
        message_dict = protobuf_to_dict(message)
        message_dict['id'] = hex(message.id)
        print prefix, message.DESCRIPTOR.name, json.dumps(message_dict, indent=4, ensure_ascii=False)


class AdminChannel(BaseChannel):

    def __init__(self, *args, **kwargs):
        self.message_manager = kwargs.pop('message_manager', None)
        super(AdminChannel, self).__init__(*args, **kwargs)

    def send(self, request):
        self.print_message(request, 'Request:')
        request_message = request.SerializeToString()
        checksum = binascii.crc32( request_message ) & 0xffffffff
        checksum = checksum % 8520
        checksum = checksum * 1087
        checksum = checksum % 255
        head = struct.pack('!HBBH', request.id, checksum, 0, len(request_message) + self.header_length)
        self._get_connection().sendall(head + request_message)

    def _do_handle(self):
        """
        there is no label/tag or any other thing to ensure wether message is a request or response.
        so, check response first, otherwise, check handle as request
        """
        head_buf = self.message_buf[:self.header_length]
        message_id, sequence, flags, length = struct.unpack_from('!HBBH', head_buf)
        if length > len(self.message_buf):
            return
        body_buf = self.message_buf[self.header_length:length]
        self.message_buf = self.message_buf[length:]
        if message_id == utils_pb2.eMessageUtils_ErrorCode_S: # error
            error_message = utils_pb2.MessageUtilsErrorCode()
            error_message.ParseFromString(body_buf)
            self.print_message(error_message.result, 'Error:')
        else:
            response = self.pending_response.get(message_id, None)
            if response:
                response.set(body_buf)
            else:
                if self.message_manager is None:
                    print "Response:", (hex(message_id), "no 'message_manager' supplied")
                    return
                message_cls = self.message_manager._message_ids[message_id]
                message = message_cls()
                message.ParseFromString(body_buf)
                self.print_message(message, "Response:")


class GatewayChannel(BaseChannel):

    def __init__(self, *args, **kwargs):
        self.message_manager = kwargs.pop('message_manager', None)
        super(GatewayChannel, self).__init__(*args, **kwargs)

    def _do_handle(self):
        """
        there is no label/tag or any other thing to ensure wether message is a request or response.
        so, check response first, otherwise, check handle as request
        """
        head_buf = self.message_buf[:self.header_length]
        message_id, sequence, flags, length = struct.unpack_from('!HBBH', head_buf)
        if length > len(self.message_buf):
            return
        body_buf = self.message_buf[self.header_length: self.header_length + length]
        self.message_buf = self.message_buf[self.header_length + length:]
        if message_id == utils_pb2.eMessageUtils_ErrorCode_S: # error
            error_message = utils_pb2.MessageUtilsErrorCode()
            error_message.ParseFromString(body_buf)
            self.print_message(error_message, 'error:')
        else:
            response = self.pending_response.get(message_id, None)
            if response:
                response.set(body_buf)
            else:
                if self.message_manager is None:
                    print "Response:", (hex(message_id), "no 'message_manager' supplied")
                    return
                message_cls = self.message_manager._message_ids[message_id]
                message = message_cls()
                message.ParseFromString(body_buf)
                self.print_message(message, 'Response:')

    def send(self, request):
        self.print_message(request, 'Request:')
        serializered_message = request.SerializeToString()
        checksum = binascii.crc32(serializered_message) & 0xffffffff
        checksum = checksum % 8520
        checksum = checksum * 1087
        checksum = checksum % 255
        head = struct.pack('!HBBH', request.id, checksum, 0, len(serializered_message))
        self._get_connection().sendall(head + serializered_message)
