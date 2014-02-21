import struct
import binascii
import json
import time

from google.protobuf import text_format

import gevent
from gevent import core
from gevent import Greenlet
from gevent import socket
from gevent import sleep
from gevent.hub import get_hub
from gevent.event import AsyncResult
from gevent.event import Event
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


class GatewayChannel(object):
    def __init__(self, host=None, port=None, service=None, **kwargs):
        self.pending_response = {}
        self.host = host
        self.port = port
        self.hub = get_hub()
        self.loop = self.hub.loop
        self.message_buf = ''
        self.max_length = 5000
        self.header_length = struct.calcsize('!HBBH')
        self.socket = None
        self.message_manager = kwargs.pop('message_manager', None)
        gevent.spawn(self._heartbeat)
        gevent.spawn(self._do_read)

    def check_connection(self):
        if self.socket is None:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.host, self.port))
            self.socket = sock

    def _do_read(self):
        while True:
            self.check_connection()
            self.message_buf += self.socket.recv(self.max_length)
            while len(self.message_buf) >= self.header_length:
                self._do_handle()

    def print_message(self, message, prefix='Message:', **kwargs):
        message_dict = protobuf_to_dict(message)
        message_dict['id'] = hex(message.id)
        message_dict.update(kwargs)
        print prefix, message.DESCRIPTOR.name, json.dumps(message_dict, indent=4, ensure_ascii=False)

    def get_checksum(self, message):
        checksum = binascii.crc32( message ) & 0xffffffff
        checksum = checksum % 8520
        checksum = checksum * 1087
        checksum = checksum % 255
        return checksum

    def _do_handle(self):
        """
        there is no label/tag or any other thing to ensure wether message is a request or response.
        so, check response first, otherwise, check handle as request
        """
        head_buf = self.message_buf[:self.header_length]
        message_id, sequence, flags, length = struct.unpack_from('!HBBH', head_buf)
        if length + self.header_length > len(self.message_buf):
            return
        body_buf = self.message_buf[self.header_length: self.header_length + length]
        self.message_buf = self.message_buf[self.header_length + length:]
        if message_id == utils_pb2.eMessageUtils_ErrorCode_S: # error
            error_message = utils_pb2.MessageUtilsErrorCode()
            error_message.ParseFromString(body_buf)
            self.print_message(error_message, 'Error:', result=hex(error_message.result))
        elif message_id == utils_pb2.eMessageUtils_Ping_CS: # heartbeat
            pass
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
        head = struct.pack('!HBBH', request.id, self.get_checksum(serializered_message), 0, len(serializered_message))
        self.check_connection()
        self.socket.sendall(head + serializered_message)

    def _heartbeat(self):
        while True:
            ping = utils_pb2.MessageUtilsPing()
            ping.timestamp1 = int(time.time())
            ping_message = ping.SerializeToString()
            head = struct.pack('!HBBH', ping.id, self.get_checksum(ping_message), 0, len(ping_message))
            self.check_connection()
            self.socket.sendall(head + ping_message)
            sleep(30)
