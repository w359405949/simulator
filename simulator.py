#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import codecs
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(codecs.open('config.ini', 'r', 'utf-8-sig'))
prototype_file = config.get('Global', 'prototype', 'prototype')
os.system('cd %s;svn up' % prototype_file)
os.system("cd %s;find . -name '*.proto' |xargs protoc --python_out=." % prototype_file)
open('%s/__init__.py' % prototype_file, 'w')

sys.modules['prototype'] = __import__(prototype_file)

from message_manager import MessageManager
from gevent import sleep
import login

def main():
    manager = MessageManager()
    manager.scan_messages('prototype/*.py')

    gateway_channel = login.auto_login(
            host=str(config.get('GatewayServer', 'host', '192.168.78.132')),
            port=int(config.get('GatewayServer', 'port', '12003')),
            account=config.get('GatewayServer', 'account'),
            rolename=config.get('GatewayServer', 'rolename'),
            soldierid=int(config.get('GatewayServer', 'soldierid', 11101000)),
            manager=manager)

    try:
        while True:
            message_name = raw_input('Enter the MessageName(Full): ')
            if message_name == '':
                continue
            if message_name in manager._fuzzy_search.keys():
                message_full_names = manager._fuzzy_search[message_name]
                if len(message_full_names) > 1:
                    print "%s in %s means:%s" % (message_name, len(message_full_names), message_full_names)
                message_name = message_full_names[0]
            message = manager.build_message(message_name)
            gateway_channel.send(message)
    except:
        print "\n"


if __name__ == "__main__":
    main()
