from google.protobuf import text_format
from gevent import sleep

from service import GatewayChannel
from service import BaseAsyncResult

from message_manager import MessageManager
from prototype.role_pb2 import *

def auto_login(host, port, account, soldierid, rolename, zoneid=0, manager=None):
    gateway_channel = GatewayChannel(message_manager=manager, host=host, port=port)

    role_list_id = MessageRoleList.DESCRIPTOR.fields_by_name['id'].default_value
    new_born_role_id = MessageNewbornRole.DESCRIPTOR.fields_by_name['id'].default_value
    role_list_result = BaseAsyncResult(MessageRoleList)
    new_born_role_result = BaseAsyncResult(MessageNewbornRole)

    gateway_channel.pending_response[role_list_id] = role_list_result
    gateway_channel.pending_response[new_born_role_id] = new_born_role_result

    message_role_login = MessageRoleLogin()
    message_role_login.account = account
    message_role_login.zoneid = zoneid
    gateway_channel.send(message_role_login)

    message_role_list = role_list_result.get()
    if len(message_role_list.infos) == 0:
        message_create_role = MessageCreateRole()
        message_create_role.rolename = rolename
        message_create_role.soldierid = soldierid
        message_create_role.account = account
        gateway_channel.send(message_create_role)
        message_new_born_role = new_born_role_result.get()
        role = message_new_born_role.role
    else:
        role = message_role_list.infos[0]
    message_role_enter_game = MessageRoleEnterGame()
    message_role_enter_game.unitid = role.unitid
    gateway_channel.send(message_role_enter_game)
    gateway_channel.host = host
    gateway_channel.port = port
    gateway_channel.soldierid = role.race
    gateway_channel.rolename = role.name
    gateway_channel.unitid = role.unitid
    gateway_channel.zoneid = zoneid
    gateway_channel.login_url = 'http://fight.o.kingnet.com/beta.php?c=test&a=test&server=%s&port=%s&oid2=%s' % (host, port, account)
    return gateway_channel

if __name__ == "__main__":
    auto_login(host='192.168.85.58', port=12005, account='yxyxyxyy', rolename='majia-222', soldierid=11101000)
