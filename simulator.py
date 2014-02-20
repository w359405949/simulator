#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from message_manager import MessageManager
from gevent import sleep
import login

def main():
    manager = MessageManager()
    manager.scan_messages('prototype/*.py')

    gateway_channel = login.auto_login(
            host='192.168.85.58',
            port=12005,
            account='yyxx',
            rolename='majia-001',
            soldierid=11101000,
            manager=manager)

    while True:
        sleep(0.5)
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

if __name__ == "__main__":
    main()
