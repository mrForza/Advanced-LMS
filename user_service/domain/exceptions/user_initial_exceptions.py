from enum import Enum

from domain.base.exceptions import *
from domain.exceptions.constants import SMALL_INITIAL_LENGTH, BIG_INITIAL_LENGTH, INCORRECT_INITIAL_CONTENT


class UserInitialException(DomainException):
    pass


class BadLength(int, Enum):
    SMALL_LENGTH = 0,
    BIG_LENGTH = 1


class IncorrectInitialLength(UserInitialException):
    def __init__(self, type_of_len: BadLength, type_of_initial) -> None:
        message = (
            SMALL_INITIAL_LENGTH.format(type_of_initial.name.capitalize())
            if type_of_len == BadLength.SMALL_LENGTH else
            BIG_INITIAL_LENGTH.format(type_of_initial.name.capitalize())
        )
        super().__init__(message)


class IncorrectInitialContent(UserInitialException):
    def __init__(self, type_of_initial) -> None:
        super().__init__(INCORRECT_INITIAL_CONTENT.format(type_of_initial.name.capitalize()))
