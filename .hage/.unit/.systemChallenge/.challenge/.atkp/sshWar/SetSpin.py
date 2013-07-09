import sys
import termios
import random
import tty

spinner = random.choice(range(10))

#'''
if True:
        print 'hannah is a good\b dog'
        for thing in range(5):
                print '\a'
#'''
spinner = 10
'''
if True:
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] | termios.IUCLC
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        raise SystemExit
'''
#GOOD FLOW CONTROL FOR IGNORES INTEGRATE INTO SHY
if spinner == 0:
        tty.setraw(sys.stdin)
elif spinner == 1:
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
elif spinner == 1:
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] | termios.ONLRET
        termios.tcsetattr(fd, termios.TCSADRAIN, new)

#ECHOCTL
#ECHOPRT(needs icanon set)
#VKILL(input history erase??)
#ONLRET(nonewline?)
#ICANON(no idea what it is but see about it)
