import pytest
import yaml

with open('config.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


@pytest.fixture()
def elem_login():
    return data['username']


@pytest.fixture()
def elem_password():
    return data['password']


@pytest.fixture()
def elem_button_login():
    return data['button_login']


@pytest.fixture()
def logging_error():
    return data['error']


@pytest.fixture()
def error_number():
    return '401'


@pytest.fixture()
def account_name():
    return data['account_name']


@pytest.fixture()
def expected_account_name():
    return f'Hello, {data["login_valid"]}'


@pytest.fixture()
def button_color_chrome():
    return 'rgba(255, 255, 255, 1)'


@pytest.fixture()
def button_color_firefox():
    return 'rgb(255, 255, 255)'


@pytest.fixture()
def field_height():
    return '56px'
