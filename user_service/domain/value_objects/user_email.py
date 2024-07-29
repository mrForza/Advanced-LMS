import re
from typing import Any, Tuple

from domain.base.base_vo import BaseValueObject
from domain.exceptions.user_email_exceptions import *


class UserEmailValidator:
    MIN_EMAIL_LENGTH = 8

    MAX_EMAIL_LENGTH = 64

    CORRECT_SERVER_DOMAIN = 'hse'

    CORRECT_COUNTRY_DOMAIN = 'ru'

    CORRECT_EMAIL_REGEX = r'[A-Za-z0-9_]+@[A-Za-z]+\.[a-z]+'

    def validate_length(self, raw_value: str) -> None:
        if len(raw_value) < self.MIN_EMAIL_LENGTH:
            raise IncorrectEmailLength(BadEmailLength.SMALL_LENGTH)
        elif len(raw_value) > self.MAX_EMAIL_LENGTH:
            raise IncorrectEmailLength(BadEmailLength.BIG_LENGTH)

    def validate_structure(self, raw_value: str) -> None:
        if not re.fullmatch(self.CORRECT_EMAIL_REGEX, raw_value):
            raise IncorrectEmailStructure()

    def validate_server_domain(self, server_domain: str) -> None:
        if server_domain != self.CORRECT_SERVER_DOMAIN:
            raise IncorrectServerDomain()

    def validate_country_domain(self, country_domain: str) -> None:
        if country_domain != self.CORRECT_COUNTRY_DOMAIN:
            raise IncorrectCountryDomain()


class UserEmail(BaseValueObject):
    def __init__(self, raw_value: str) -> None:
        self.__validator = UserEmailValidator()
        self._validate(raw_value)
        self.__user_name, self.__server_domain, self.__country_domain = (
            self.__split_raw_email(raw_value)
        )

    def __repr__(self) -> str:
        return f'''
        UserEmail:
            user_name: {self.__user_name}
            server_domain: {self.__server_domain}
            country_domain: {self.__country_domain}
        '''

    def _validate(self, raw_value: str) -> None:
        self.__validator.validate_length(raw_value)
        self.__validator.validate_structure(raw_value)
        _, server_domain, country_domain = self.__split_raw_email(raw_value)
        self.__validator.validate_server_domain(server_domain)
        self.__validator.validate_country_domain(country_domain)

    def _get_atomic_components(self) -> Tuple[str, str, str]:
        return self.__user_name, self.__server_domain, self.__country_domain

    def __split_raw_email(self, raw_value: str) -> Tuple[str, str, str]:
        user_name = raw_value.split('@')[0]
        server_name = raw_value.split('@')[-1].split('.')[0]
        country_domain = raw_value.split('@')[-1].split('.')[-1]
        return user_name, server_name, country_domain
