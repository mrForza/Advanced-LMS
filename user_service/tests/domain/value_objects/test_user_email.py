import pytest

from domain.value_objects.user_email import UserEmailValidator
from domain.exceptions.user_email_exceptions import *


@pytest.mark.parametrize(
    'raw_value',
    ['a@a.q', 'a@bk.ru']
)
def test_email_validation_small_length(raw_value: str):  # len == 7 (less than lower bound) and len << 8
    with pytest.raises(IncorrectEmailLength):
        email_validator = UserEmailValidator()
        email_validator.validate_length(raw_value)


@pytest.mark.parametrize(
    'raw_value',
    ['a' * 60 + 'bk.ru', 'b' * 70 + 'hse.run']  # len == 65 (more than upper bound) and len >> 64
)
def test_email_validation_big_length(raw_value: str):
    with pytest.raises(IncorrectEmailLength):
        email_validator = UserEmailValidator()
        email_validator.validate_length(raw_value)


@pytest.mark.parametrize(
    'raw_value',
    ['a@hse.ru', 'a' * 57 + '@hse.ru', 'rsgromov@hse.ru']
)  # len == 8 (lower bound), len == 64 (upper bound) and 8 < len < 64
def test_email_validation_good_length(raw_value: str):
    email_validator = UserEmailValidator()
    email_validator.validate_length(raw_value)


@pytest.mark.parametrize(
    'raw_value',
    ['email_with_no_server_domain_and_country_domain', '@email_with_no_name_and_country_domain',
     '.email_with_no_name_and_server_domain', 'email_with_no_country_domain@hse', 'email_with_no_server_domain.ru',
     '@email_with_no_name.ru', '@email_with_two_at@hse.ru', '.email_with_two_dots@hse.ru', '']
)  # Set of different emails which don't have a necessary part of email, e.g. username, server domain or country code
def test_email_validation_incorrect_structure(raw_value: str):
    with pytest.raises(IncorrectEmailStructure):
        email_validator = UserEmailValidator()
        email_validator.validate_structure(raw_value)


@pytest.mark.parametrize(
    'raw_value',
    ['good_structure@hse.ru']
)  # A set of emails which have a correct structure (exists @, . username, server domain and country code)
def test_email_validation_good_structure(raw_value: str):
    email_validator = UserEmailValidator()
    email_validator.validate_structure(raw_value)


@pytest.mark.parametrize(
    'server_domain',
    ['bk', 'dom', 'yandex', 'gmail', 'hsr']
)
def test_email_validation_incorrect_server_domain(server_domain: str):
    with pytest.raises(IncorrectServerDomain):
        email_validator = UserEmailValidator()
        email_validator.validate_server_domain(server_domain)


@pytest.mark.parametrize(
    'country_domain',
    ['com', 'net', 'xyz', 'de', 'uk']
)
def test_email_validation_incorrect_country_domain(country_domain: str):
    with pytest.raises(IncorrectServerDomain):
        email_validator = UserEmailValidator()
        email_validator.validate_server_domain(country_domain)
