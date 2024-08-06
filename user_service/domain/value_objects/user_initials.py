from enum import Enum
from typing import Tuple

from domain.base.base_vo import BaseValueObject
from domain.exceptions.user_initial_exceptions import *


class TypeOfInitial(int, Enum):
    NAME = 0,
    SURNAME = 1,
    FATHER_NAME = 2


class UserInitialValidator:
    MIN_NAME_LENGTH = 2

    MAX_NAME_LENGTH = 32

    def validate_length(self, raw_value: str, type_of_initial: TypeOfInitial) -> None:
        if len(raw_value) < self.MIN_NAME_LENGTH:
            raise IncorrectInitialLength(BadLength.SMALL_LENGTH, type_of_initial)
        elif len(raw_value) > self.MAX_NAME_LENGTH:
            raise IncorrectInitialLength(BadLength.BIG_LENGTH, type_of_initial)

    def validate_symbols(self, raw_value: str, type_of_initial: TypeOfInitial) -> None:
        if raw_value.count('-') == len(raw_value):
            raise IncorrectInitialContent(type_of_initial)

        for symbol in raw_value:
            if symbol != '-' and (ord(symbol) < 65 or 90 < ord(symbol) < 97 or ord(symbol) > 122):
                raise IncorrectInitialContent(type_of_initial)


class UserInitial(BaseValueObject):
    def __init__(self, raw_value: str, **kwargs) -> None:
        self.__validator = UserInitialValidator()
        self._validate(raw_value, kwargs.get('type'))
        self._initial = raw_value
        self._type = kwargs.get('type')

    def __repr__(self) -> str:
        return f'{self._type.name.capitalize()}: {self._initial}'

    def _validate(self, *args, **kwargs) -> None:
        self.__validator.validate_length(args[0], args[1])
        self.__validator.validate_symbols(args[0], args[1])

    def _get_atomic_components(self) -> Tuple[str]:
        return self._initial,


class UserName(UserInitial):
    def __init__(self, raw_value: str):
        super().__init__(raw_value, type=TypeOfInitial.NAME)


class UserSurName(UserInitial):
    def __init__(self, raw_value: str):
        super().__init__(raw_value, type=TypeOfInitial.SURNAME)


class UserFatherName(UserInitial):
    def __init__(self, raw_value: str):
        super().__init__(raw_value, type=TypeOfInitial.FATHER_NAME)
