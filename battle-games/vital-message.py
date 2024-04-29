import os
import string
import random
import time


def clear() -> None:
    """Clears the screen."""
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def is_int(value: str) -> bool:
    """Checks if a value is an integer.

    :param str value: The value to check.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def run() -> None:
    clear()
    print('VITAL MESSAGE', '\n')

    # Keep iterating until the user selects a difficulty value between 4 and 10
    while True:
        difficulty_input = input('HOW DIFFICULT? (4-10) ')
        if is_int(difficulty_input) and 4 <= int(difficulty_input) <= 10:
            difficulty = int(difficulty_input)
            break

    # Generate the message for the user to remember
    message = ''
    for i in range(difficulty):
        message += string.ascii_uppercase[random.randint(0, 25)]

    # Display the message to the user
    clear()
    print(f'SEND THIS MESSAGE:\n\n{message}')

    # Wait for approximately half a second per character in the message
    time.sleep(difficulty * 0.5)
    clear()

    # Get the user input, convert it to upper case and strip out any spaces
    user_input = input('> ').upper().strip()

    # Check if the user remembered the vital message
    if user_input != message:
        print(f'YOU GOT IT WRONG\nYOU SHOULD HAVE SENT:\n{message}')
    else:
        print('MESSAGE CORRECT\nTHE WAR IS OVER')


if __name__ == '__main__':
    run()
