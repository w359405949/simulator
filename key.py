import curses

stdscr = curses.initscr()

direction = {ord('w'):1, ord('a'):4, ord('s'):2, ord('d'):8}
try:
    while True:
        c = stdscr.getch()
        if c == ord('j'):
            # attack
            attack_message = manager._message_classes['msg.fight.MessageAttackCommand']()
            attack_message.unitid = gateway_channel.unitid
            gateway_channel.send(attack_message)

        elif c in direction.keys():
            # run
            run_message = manager._message_classes['msg.fight.MessageRunCommand']()
            run_message.unitid = gateway_channel.unitid
            gateway_channel.send(run_message)
            dir_message = manager._message_classes['msg.fight.MessageDirectCommand']()
            dir_message.unitid = gateway_channel.unitid
            dir_message.dir = direction[c]
            gateway_channel.send(dir_message)

        elif c == ord('r'):
            # ready
            ready_message = manager._message_classes['msg.fight.MessageReadyCommand']()
            ready_message.unitid = gateway_channel.unitid
            gateway_channel.send(ready_message)

        elif c == ord('q'):
            # stop
            dir_message = manager._message_classes['msg.fight.MessageDirectCommand']()
            dir_message.unitid = gateway_channel.unitid
            dir_message.dir = 0
            gateway_channel.send(dir_message)
except:
    pass
curses.endwin()
