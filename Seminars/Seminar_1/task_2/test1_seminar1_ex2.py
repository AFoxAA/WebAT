import pytest
import requests
import yaml
from requests import Session, Response
from typing import Any

with open('config.yaml', encoding='utf-8') as f:
    data: Any = yaml.safe_load(f)

S: Session = requests.Session()


def test_step1(user_login: Any, post_title: str) -> None:
    result: Response = S.get(url=data['address'], headers={'X-Auth-Token': user_login}, params={'owner': 'notMe'})
    result_title: list = [i['title'] for i in result.json()['data']]
    assert post_title in result_title, 'test_step1 FAIL'


if __name__ == '__main__':
    pytest.main(['-vv'])
