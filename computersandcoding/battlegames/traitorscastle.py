from random import random

from computersandcoding.helpers import clear, get_user_input, is_int


def run() -> None:
    clear()

    print("TRAITOR'S CASTLE")

    s = 0
    for g in range(1, 11):
        r = ''
        t = int(random() * 9 + 1)

        for p in range(1, 10):
            if p == t:
                r += 'O '
            else:
                r += '. '

        print(r)
        i = get_user_input('', timeout=(2 + random()))

        if i is not None and is_int(i) and int(i) == t:
            print('GOOD SHOT')
            s += 1
        else:
            print('MISSED')

    print(f'YOU HIT {s} OUT OF 10')
