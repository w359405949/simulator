#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import readline
import codecs
import ConfigParser

import patches
patches.patch_prototype()

from message_manager import MessageManager
from gevent import sleep
from gevent.socket import wait_read
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
                self.matches.extend(s for s in self.message_manager._fuzzy_search.keys() if s.startswith(text))
                self.matches.extend(f for f in os.listdir('.') if f.startswith(text) and f.endswith('.py'))
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
    manager._ignore_messages.extend(message.strip() for message in config.get('Message', 'ignore', '').split(','))
    manager._skip_fields.extend(field.strip() for field in config.get('Message', 'skip', '').split(','))
    manager.scan_messages('%s/*.py' % prototype_file)

    readline.parse_and_bind("tab: complete")
    readline.set_completer(MessageCompleter(manager).complete)
    history_file = config.get('History', 'file', '.message_history')
    open(history_file, 'w').close()
    readline.read_history_file(history_file)

    gateway_channel = login.auto_login(
            host=str(config.get('GatewayServer', 'host', '192.168.78.132')),
            port=int(config.get('GatewayServer', 'port', '12003')),
            account=config.get('GatewayServer', 'account'),
            rolename=config.get('GatewayServer', 'rolename'),
            soldierid=int(config.get('GatewayServer', 'soldierid', 11101000)),
            manager=manager)

    while True:
        sleep(0.1)
        message_name = ''
        try:
            print gateway_channel.login_url
            print '%s@%s:%s, %s(%s)' % (gateway_channel.unitid, gateway_channel.host, gateway_channel.port, gateway_channel.rolename, gateway_channel.soldierid)
            message_name = raw_input('Enter the MessageName(Full): ')
            message_name = message_name.strip()
            if message_name in manager._fuzzy_search.keys():
                message_full_names = manager._fuzzy_search[message_name]
                if len(message_full_names) > 1:
                    print "%s in %s means:%s" % (message_name, len(message_full_names), message_full_names)
                message_name = message_full_names[0]

            if message_name in manager._message_classes.keys():
                message = manager.build_message(message_name)
                gateway_channel.send(message)
            elif message_name.startswith('#'):
                message_cls = manager._message_classes.get('msg.role.MessageRoleChat', None)
                if message_cls:
                    message = message_cls()
                    message.message = message_name
                    gateway_channel.send(message)
                else:
                    print 'gmcommand not support'
            elif message_name.startswith('$'):
                if message_name == '$sleep':
                    try:
                        while True:
                            sleep(1)
                    except:
                        pass
                elif message_name.startswith('$run '):
                    try:
                        file_name = message_name.split(' ')[1]
                        print 'run:', file_name
                        execfile(file_name)
                    except Exception as e:
                        print e, type(e)
            else:
                if message_name:
                    print '%s: not found' % message_name

        except EOFError as e:
            print '\n'
            exit()
        except:
            '\n'
            pass
        finally:
            readline.write_history_file(history_file)

if __name__ == "__main__":
    main()
