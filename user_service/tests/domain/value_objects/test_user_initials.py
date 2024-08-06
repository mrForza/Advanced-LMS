import pytest

from domain.exceptions.user_initial_exceptions import *
from domain.value_objects.user_initials import UserInitialValidator, TypeOfInitial


@pytest.mark.parametrize(
    'initial',
    ['', 'a']
)
def test_initials_validation_small_length(initial: str):
    with pytest.raises(IncorrectInitialLength):
        UserInitialValidator().validate_length(initial, TypeOfInitial.NAME)


@pytest.mark.parametrize(
    'initial',
    ['a' * 33, 'a' * 40]
)
def test_initials_validation_big_length(initial: str):
    with pytest.raises(IncorrectInitialLength):
        UserInitialValidator().validate_length(initial, TypeOfInitial.NAME)


@pytest.mark.parametrize(
    'initial',
    ['a' * 2, 'a' * 32, 'a' * 10]
)
def test_initials_validation_correct_length(initial: str):
    UserInitialValidator().validate_length(initial, TypeOfInitial.NAME)


@pytest.mark.parametrize(
    'initial',
    ['R0man', '1nna', '123123', '!@#$%^&*', '----']
)
def test_initials_validation_bad_content(initial: str):
    with pytest.raises(IncorrectInitialContent):
        UserInitialValidator().validate_symbols(initial, TypeOfInitial.NAME)


@pytest.mark.parametrize(
    'initial',
    ['Roman', 'Kirill', 'Io', 'Vladislav', 'Maryam-El-Vakil']
)
def test_initials_validation_correct(initial: str):
    UserInitialValidator().validate_symbols(initial, TypeOfInitial.NAME)
