from enum import Enum

from domain.base.exceptions import DomainException
from domain.exceptions.constants import (
    SMALL_PASSWORD_LENGTH_MESSAGE, BIG_PASSWORD_LENGTH_MESSAGE, NO_LOWER_CASE_SYMBOLS_MESSAGE,
    NO_UPPER_CASE_SYMBOLS_MESSAGE, NO_DIGITS_MESSAGE, NO_SPECIAL_SYMBOLS_MESSAGE
)


class BadLengthType(int, Enum):
    SMALL_LENGTH = 0,
    BIG_LENGTH = 1


class PasswordException(DomainException):
    pass


class IncorrectPasswordLength(PasswordException):
    def __init__(self, type_of_len: BadLengthType) -> None:
        message = (SMALL_PASSWORD_LENGTH_MESSAGE if type_of_len.value == 0 else BIG_PASSWORD_LENGTH_MESSAGE)
        super().__init__(message)


class IncorrectPasswordContent(PasswordException):
    pass


class NoUppercaseLettersInPassword(IncorrectPasswordContent):
    def __init__(self) -> None:
        super().__init__(NO_LOWER_CASE_SYMBOLS_MESSAGE)


class NoLowercaseLettersInPassword(IncorrectPasswordContent):
    def __init__(self) -> None:
        super().__init__(NO_UPPER_CASE_SYMBOLS_MESSAGE)


class NoSpecialSymbolsInPassword(IncorrectPasswordContent):
    def __init__(self) -> None:
        super().__init__(NO_DIGITS_MESSAGE)


class NoDigitsInPassword(IncorrectPasswordContent):
    def __init__(self) -> None:
        super().__init__(NO_SPECIAL_SYMBOLS_MESSAGE)
