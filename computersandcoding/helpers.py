import os
from typing import Union

from inputimeout import inputimeout, TimeoutOccurred


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


def get_user_input(prompt: str, timeout: float) -> Union[str, None]:
    try:
        return inputimeout(prompt=prompt, timeout=timeout)
    except TimeoutOccurred:
        return None
