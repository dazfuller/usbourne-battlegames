import random
import string

from computersandcoding.helpers import clear


def run() -> None:
    clear()

    print('ROBOT MISSILE\n')
    print('TYPE THE CORRECT LETTER')
    print('LETTER (A-Z) TO')
    print('DEFUSE THE MISSILE.')
    print('YOU HAVE 4 CHANCES')

    secret_char = string.ascii_uppercase[random.randint(0, 25)]

    for i in range(4):
        while True:
            guess = input('> ').strip()
            if len(guess) > 0 and guess in string.ascii_uppercase:
                guess = guess[0]
                break
        if guess < secret_char:
            print(f'LATER THAN {guess}')
        elif guess > secret_char:
            print(f'EARLIER THAN {guess}')
        else:
            print('TICK...FZZZ...CLICK...')
            print('YOU DID IT')
            return

    print('\nBOOOOOOOMMM...')
    print('YOU BLEW IT.')
    print(f'THE CORRECT CODE WAS {secret_char}')
