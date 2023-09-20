import os
import pytest
import requests
import yaml
from dotenv import load_dotenv
from requests import Response, Session
from typing import Any

with open('config.yaml', encoding='utf-8') as f:
    data: Any = yaml.safe_load(f)

S: Session = requests.Session()


@pytest.fixture()
def user_login() -> Any:
    '''Логирование пользователя на сайте, получение токена'''
    load_dotenv()
    result: Response = S.post(url=data['url'], data={'username': os.getenv('login'), 'password': os.getenv('password')})
    response_json: Any = result.json()
    token: Any = response_json.get('token')
    return token


@pytest.fixture()
def post_title() -> str:
    '''Тестовая фраза для тестирования 1-ого теста'''
    return data['post_title']


@pytest.fixture()
def creating_a_post() -> dict[str, str]:
    '''Тестовые данные полей'''
    return data['post_data']


@pytest.fixture()
def post_presence_by_description() -> str:
    '''Тестовая фраза для тестирования 2-ого теста'''
    return data['post_presence_by_description']
