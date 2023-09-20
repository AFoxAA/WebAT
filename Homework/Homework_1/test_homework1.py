import pytest
import requests
import yaml
from requests import Session, Response
from typing import Any

with open('config.yaml', encoding='utf-8') as f:
    data: Any = yaml.safe_load(f)

S: Session = requests.Session()


def test_step1(user_login: Any, post_title: str) -> None:
    '''Проверка, что тестовая фраза присутствует в списке ответа'''
    result: Response = S.get(url=data['address'], headers={'X-Auth-Token': user_login}, params={'owner': 'notMe'})
    result_title: list = [i['title'] for i in result.json()['data']]
    assert post_title in result_title, 'test_step1 FAIL'


def test_step2(user_login: Any, creating_a_post: dict[str, str], post_presence_by_description: str) -> None:
    '''Создание поста и проверка, что дестовая фраза поля "descriptions" присутствует в списке ответа'''
    S.post(url=data['address'], headers={'X-Auth-Token': user_login}, data=creating_a_post)

    response_result: Response = S.get(url=data['address'], headers={'X-Auth-Token': user_login})
    descriptions: list = [i['description'] for i in response_result.json()['data']]
    assert post_presence_by_description in descriptions, 'Fail test_step2'


if __name__ == '__main__':
    pytest.main(['-vv'])
