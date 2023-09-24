import pytest
import yaml

with open('config.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


@pytest.fixture()
def error_number():
    return '401'


@pytest.fixture()
def field_height():
    return '56px'


@pytest.fixture()
def button_color_chrome():
    return 'rgba(255, 255, 255, 1)'


@pytest.fixture()
def button_color_firefox():
    return 'rgb(255, 255, 255)'


@pytest.fixture()
def expected_account_name():
    return f'Hello, {data["login_valid"]}'


@pytest.fixture()
def field_title():
    return 'Тестовый пост №5'


@pytest.fixture()
def field_description():
    return 'Описание тестового поста №5'


@pytest.fixture()
def field_content():
    return 'Создание пробного поста c помощью Selenium WebDriver Python'
