from google.protobuf import text_format
from prototype.gm_pb2 import *
from service import AdminChannel
from message_manager import MessageManager
from pb_to_dict import protobuf_to_dict

import json

def main():
    manager = MessageManager()
    manager.scan_messages('protocol/*.py')
    admin_channel = AdminChannel(message_manager=manager, host='192.168.85.58', port=20005)
    request = MessageGMGetRoleInfoRequest()
    request.roleid = 72057594037973882
    response = admin_channel.send(request)
    #text_response = text_format.MessageToString(response)
    #text_response = text_response.replace(' ', '')
    #text_response = text_response.replace('{\n', '{')
    #text_response = text_response.replace('\n}', '}')
    #text_response = text_response.replace('}\n', '},')
    #text_response = text_response.replace('\n', ' ')
    #text_response = text_response.replace('},', '}\n')
    #text_response = text_response.replace(':', '=')

if __name__ == "__main__":
    main()
