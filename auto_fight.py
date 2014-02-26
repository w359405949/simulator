from random import randint
from random import uniform

print 'start fight'
while True:

    # attack
    attack_message = manager._message_classes['msg.fight.MessageAttackCommand']()
    attack_message.unitid = gateway_channel.unitid
    for i in xrange(randint(20, 50)):
        sleep(uniform(0.1, 0.3))
        gateway_channel.send(attack_message)

    # run
    run_message = manager._message_classes['msg.fight.MessageRunCommand']()
    run_message.unitid = gateway_channel.unitid
    gateway_channel.send(run_message)
    dir_message = manager._message_classes['msg.fight.MessageDirectCommand']()
    dir_message.unitid = gateway_channel.unitid
    dir_message.dir = int(uniform(1.7, 2.9)) * 4
    gateway_channel.send(dir_message)

    sleep(uniform(0.3, 1))

    # ready
    for i in xrange(2):
        ready_message = manager._message_classes['msg.fight.MessageReadyCommand']()
        ready_message.unitid = gateway_channel.unitid
        gateway_channel.send(ready_message)
