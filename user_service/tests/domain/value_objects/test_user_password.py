from random import randrange

import pytest

from domain.value_objects.user_password import UserPasswordValidator
from domain.exceptions.user_password_exceptions import *
from domain.exceptions.constants import *


@pytest.mark.parametrize(
    'raw_value',
    [''.join([chr(randrange(97, 122 + 1)) for _ in range(0, length)]) for length in range(0, 7 + 1)]
)
def test_password_validation_small_length(raw_value: str):
    with pytest.raises(IncorrectPasswordLength, match=SMALL_PASSWORD_LENGTH_MESSAGE):
        password_validator = UserPasswordValidator()
        password_validator.validate_length(raw_value)


@pytest.mark.parametrize(
    'raw_value',
    [''.join([chr(randrange(97, 122 + 1)) for _ in range(0, length)]) for length in range(65, 70)]
)
def test_password_validation_big_length(raw_value: str):
    with pytest.raises(IncorrectPasswordLength, match=BIG_PASSWORD_LENGTH_MESSAGE):
        password_validator = UserPasswordValidator()
        password_validator.validate_length(raw_value)


@pytest.mark.parametrize(
    'raw_value',
    ['PASSWORD_WITH_NO_LOWER_SYMBOLS123_+']
)
def test_password_validation_no_lower_symbols(raw_value: str):
    with pytest.raises(NoLowercaseLettersInPassword):
        password_validator = UserPasswordValidator()
        password_validator.validate_symbols(raw_value)


@pytest.mark.parametrize(
    'raw_value',
    ['password_with_no_upper_symbols123_+']
)
def test_password_validation_no_upper_symbols(raw_value: str):
    with pytest.raises(NoUppercaseLettersInPassword):
        password_validator = UserPasswordValidator()
        password_validator.validate_symbols(raw_value)


@pytest.mark.parametrize(
    'raw_value',
    ['PASSWORD_with_NO_digits_+']
)
def test_password_validation_no_digits(raw_value: str):
    with pytest.raises(NoDigitsInPassword):
        password_validator = UserPasswordValidator()
        password_validator.validate_symbols(raw_value)


@pytest.mark.parametrize(
    'raw_value',
    ['PASSWORD with NO special SYMBOLS 123']
)
def test_password_validation_no_special_symbols(raw_value: str):
    with pytest.raises(NoSpecialSymbolsInPassword):
        password_validator = UserPasswordValidator()
        password_validator.validate_symbols(raw_value)
