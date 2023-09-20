import pytest
from api_utils import check_text


def test_step1(valid_word, invalid_word) -> None:
    assert valid_word in check_text(invalid_word), 'test_step1 FAIL'


if __name__ == '__main__':
    pytest.main(['-vv'])
