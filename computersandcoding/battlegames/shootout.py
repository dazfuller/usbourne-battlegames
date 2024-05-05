from random import random
from time import sleep
from typing import Union

from inputimeout import inputimeout, TimeoutOccurred

from computersandcoding.helpers import clear


def get_user_input(prompt: str, timeout: float) -> Union[str, None]:
    try:
        return inputimeout(prompt=prompt, timeout=timeout)
    except TimeoutOccurred:
        return None


def run() -> None:
    clear()

    print('COWBOY SHOOTOUT -')
    print('YOU ARE BACK TO BACK')
    print('TAKE 10 PACES...')

    for i in range(1, 11):
        print(i, '..')
        sleep(0.7)

    print()
    cheated = False
    user_input = None

    # Check to see if the user has pressed enter during the countdown, if so then they are too early and
    # have cheated
    if get_user_input('', 0.001) is not None:
        cheated = True

    # If the user has not pressed any kep so far then wait between 0 and 0.5 seconds for them to press enter
    print('HE DRAWS....')
    if not cheated:
        user_input = get_user_input('', random() * 0.5)

    # If the user didn't press enter in time, or cheated, then they are dead
    if cheated or user_input is None:
        print('AND SHOOTS.')
        if cheated:
            print('YOU CHEATED AND YOUR GUN JAMS.')
        print('YOU ARE DEAD.')
    else:
        print('BUT YOU SHOOT FIRST.')
        print('YOU KILLED HIM.')
