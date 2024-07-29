import hashlib
from typing import Any, Tuple

from domain.base.base_vo import BaseValueObject
from domain.exceptions.user_password_exceptions import *


class UserPasswordValidator:
    MINIMAL_PASSWORD_LENGTH = 8

    MAXIMUM_PASSWORD_LENGTH = 64

    SPECIAL_SYMBOLS = set('!@#$%^&*()_+-=/.,')

    LOWERCASE_LETTERS = set([chr(code) for code in range(97, 122 + 1)])

    UPPERCASE_LETTERS = set([chr(code) for code in range(65, 90 + 1)])

    DIGITS = set('0123456789')

    def validate_length(self, raw_value: str) -> None:
        if len(raw_value) < self.MINIMAL_PASSWORD_LENGTH:
            raise IncorrectPasswordLength(BadLengthType.SMALL_LENGTH)
        elif len(raw_value) > self.MAXIMUM_PASSWORD_LENGTH:
            raise IncorrectPasswordLength(BadLengthType.BIG_LENGTH)

    def validate_symbols(self, raw_value) -> None:
        unique_symbols = set(raw_value)

        if not unique_symbols.intersection(self.LOWERCASE_LETTERS):
            raise NoLowercaseLettersInPassword()

        if not unique_symbols.intersection(self.UPPERCASE_LETTERS):
            raise NoUppercaseLettersInPassword()

        if not unique_symbols.intersection(self.SPECIAL_SYMBOLS):
            raise NoSpecialSymbolsInPassword()

        if not unique_symbols.intersection(self.DIGITS):
            raise NoDigitsInPassword()


class UserPassword(BaseValueObject):
    def __init__(self, raw_value: str) -> None:
        self.__validator = UserPasswordValidator()
        self._validate(raw_value)
        self.__hashed_value = self.__make_hashed_value(raw_value)

    def __repr__(self) -> str:
        return f'UserPassword: {self.__hashed_value}'

    def _get_atomic_components(self) -> Tuple[Any]:
        return self.__hashed_value,

    def _validate(self, raw_value: str) -> None:
        self.__validator.validate_length(raw_value)
        self.__validator.validate_symbols(raw_value)

    def __make_hashed_value(self, raw_value: str) -> str:
        hashed_object = hashlib.new('sha256')
        hashed_object.update(raw_value.encode())
        return hashed_object.hexdigest()
