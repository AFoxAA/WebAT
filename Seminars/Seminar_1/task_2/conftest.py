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
    load_dotenv()
    result: Response = S.post(url=data['url'], data={'username': os.getenv('login'), 'password': os.getenv('password')})
    response_json: Any = result.json()
    token: Any = response_json.get('token')
    return token


@pytest.fixture()
def post_title() -> str:
    return 'тест отложенной публикации'

# @pytest.fixture()
# def user_login() -> Any:
#     result: Response = S.post(url=data['url'], data={'username': data['your_login'], 'password': data['your_pass']})
#     response_json: Any = result.json()
#     token: Any = response_json.get('token')
#     return token
