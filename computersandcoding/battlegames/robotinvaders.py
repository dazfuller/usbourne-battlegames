from random import random, choice
from time import sleep

from computersandcoding.helpers import clear, get_user_input


def run() -> None:
    clear()

    print('ROBOT INVADERS')

    h = 0
    for _ in range(25):
        sleep(1.5)

        a = int(random() * 20)
        d = int(random() * 15)
        p = choice(['U', 'V', 'W', 'X', 'Y'])   # A bit different to the original, but easier to see what's happening

        clear()

        for _ in range(d):
            print()

        print(' ' * a, p)
        r = get_user_input('> ', 1.3)

        if r == p:
            print('A HIT')
            h += 1
        else:
            print('MISSED')

    print('YOU SCORED ', h, '/25')
