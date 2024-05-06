import math
from random import random

from computersandcoding.helpers import clear, is_int


def get_int_input(prompt: str) -> int:
    print(prompt)
    while True:
        value = input('> ')
        if is_int(value):
            return int(value)


def run() -> None:
    clear()

    print('DESERT TANK BATTLE')

    # Selects a random direction and distance for the enemy stronghold
    direction = int((random() * 181) - 90)
    distance = random()

    for guess in range(0, 5):
        user_direction = get_int_input('DIRECTION (-90 TO 90) ?')
        user_elevation = get_int_input('ELEVATION (0 TO 90) ?')

        user_distance = math.sin(2 * (user_elevation / 180 * 3.1416))

        if abs(direction - user_direction) < 2 and abs(distance - user_distance) < 0.05:
            print('*KABOOOMMM*')
            print("YOU'VE DONE IT")
            return

        print('MISSILE LANDED ', end='')

        if user_direction < direction:
            print('TO THE LEFT ', end='')
        elif user_direction > direction:
            print('TO THE RIGHT ', end='')

        if abs(user_distance - distance) > 0.05 and user_direction != direction:
            print('AND ', end='')

        if distance - user_distance > 0.05:
            print('NOT FAR ENOUGH')
        elif user_distance - distance > 0.05:
            print('TOO FAR')

        print('\n')

    print('DISASTER - YOU FAILED')
    print('RETREAT IN DISGRACE')
