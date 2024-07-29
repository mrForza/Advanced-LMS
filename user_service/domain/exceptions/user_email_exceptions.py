from enum import Enum

from domain.base.exceptions import DomainException
from domain.exceptions.constants import (
    SMALL_EMAIL_LENGTH_MESSAGE, BIG_EMAIL_LENGTH_MESSAGE, INCORRECT_EMAIL_STRUCTURE_MESSAGE,
    INCORRECT_SERVER_DOMAIN, INCORRECT_COUNTRY_DOMAIN
)


class UserEmailException(DomainException):
    pass


class BadEmailLength(int, Enum):
    SMALL_LENGTH = 0,
    BIG_LENGTH = 1


class IncorrectEmailLength(UserEmailException):
    def __init__(self, type_of_len: BadEmailLength) -> None:
        message = (SMALL_EMAIL_LENGTH_MESSAGE if type_of_len == BadEmailLength.SMALL_LENGTH
                   else BIG_EMAIL_LENGTH_MESSAGE)
        super().__init__(message)


class IncorrectEmailStructure(UserEmailException):
    def __init__(self) -> None:
        super().__init__(INCORRECT_EMAIL_STRUCTURE_MESSAGE)


class IncorrectServerDomain(UserEmailException):
    def __init__(self) -> None:
        super().__init__(INCORRECT_SERVER_DOMAIN)


class IncorrectCountryDomain(UserEmailException):
    def __init__(self) -> None:
        super().__init__(INCORRECT_COUNTRY_DOMAIN)
