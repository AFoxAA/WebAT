import pytest


@pytest.fixture()
def valid_word() -> str:
    return 'молоко'


@pytest.fixture()
def invalid_word() -> str:
    return 'малоко'
