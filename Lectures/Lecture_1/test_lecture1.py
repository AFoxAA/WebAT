import pytest
from api_utils import get_sites


def test_step1(coord1, text, limit, radius) -> None:
    assert text in get_sites(coord1[0], coord1[1], limit, radius), 'test_step1 FAIL'


if __name__ == '__main__':
    pytest.main(['-vv'])
