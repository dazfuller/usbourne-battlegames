import os


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
