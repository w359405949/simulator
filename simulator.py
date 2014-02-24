#!/usr/bin/env python
# -*- coding: utf-8 -*-
import readline
import codecs
import ConfigParser

import patches
patches.patch_prototype()

from message_manager import MessageManager
from gevent import sleep
import login


class MessageCompleter(object):

    def __init__(self, message_manager):
        self.message_manager = message_manager

    def complete(self, text, state):
        text = text.strip()
        response = None
        if state == 0:
            self.matches = []
            if text:
                self.matches.extend(s for s in self.message_manager._fuzzy_search.keys()
                        if s.startswith(text))
        try:
            response = self.matches[state]
        except:
            pass
        return response

def main():
    config = ConfigParser.ConfigParser()
    config.readfp(codecs.open('config.ini', 'r', 'utf-8-sig'))
    prototype_file = config.get('Global', 'prototype', 'prototype')

    manager = MessageManager()
    manager.scan_messages('%s/*.py' % prototype_file)

    gateway_channel = login.auto_login(
            host=str(config.get('GatewayServer', 'host', '192.168.78.132')),
            port=int(config.get('GatewayServer', 'port', '12003')),
            account=config.get('GatewayServer', 'account'),
            rolename=config.get('GatewayServer', 'rolename'),
            soldierid=int(config.get('GatewayServer', 'soldierid', 11101000)),
            manager=manager)

    readline.parse_and_bind("tab: complete")
    readline.set_completer(MessageCompleter(manager).complete)
    while True:
        message_name = ''
        try:
            message_name = raw_input('Enter the MessageName(Full): ')
        except EOFError as e:
            print '\n'
            exit()
        except:
            print '\n'
            pass
        message_name = message_name.strip()
        if message_name == '':
            continue
        if message_name in manager._fuzzy_search.keys():
            message_full_names = manager._fuzzy_search[message_name]
            if len(message_full_names) > 1:
                print "%s in %s means:%s" % (message_name, len(message_full_names), message_full_names)
            message_name = message_full_names[0]
        if message_name in manager._message_classes.keys():
            message = manager.build_message(message_name)
            gateway_channel.send(message)
        else:
            print '%s: not found' % message_name


if __name__ == "__main__":
    main()
