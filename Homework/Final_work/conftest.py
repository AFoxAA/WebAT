import logging
from typing import Any, Generator
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Homework_4 import SoapAPI

with open('config.yaml', encoding='utf-8') as file:
    file_data: Any = yaml.safe_load(file)
    browser: Any = file_data['browser']
    sleep: Any = file_data['sleep']


@pytest.fixture(scope='session')
def initialize_web_driver() -> Generator:
    driver = None

    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(service=service, options=options)

    elif browser == 'chrome':
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(sleep)

    yield driver

    driver.quit()


@pytest.fixture()
def api_page():
    with open('config.yaml', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    if not data['wsdl']:
        logging.exception("Отсутствует ссылка на WSDL в config.yaml")
        return None

    try:
        return SoapAPI(wsdl_url=data['wsdl'])
    except Exception:
        logging.exception(f"Ошибка подключения к WSDL: проверьте корректность ссылки")
        return None


@pytest.fixture()
def checking_correct_word():
    return 'ЗАПУСК ПОЗИТИВНОГО ТЕСТА ДЛЯ ПРОВЕРКИ СЛОВА'


@pytest.fixture()
def valid_word() -> str:
    return 'молоко'


@pytest.fixture()
def invalid_word() -> str:
    return 'малоко'


@pytest.fixture()
def post_creation_check():
    return 'ЗАПУСК ПОЗИТИВНОГО ТЕСТА ДЛЯ ПРОВЕРКИ СОЗДАНИЯ ПОСТА С ПОМОЩЬЮ RESTAPI'


@pytest.fixture()
def test_data():
    data_for_post = {"title": "Тестовый пост №5",
                     "description": "Создание пробного поста по API c помощью Python",
                     "content": "Домашнее задание №1"}

    return data_for_post


@pytest.fixture()
def post_presence_by_description() -> str:
    return 'Создание прбного поста по API c помощью Python'


@pytest.fixture()
def invalid_login() -> str:
    return 'ЗАПУСК НЕГАТИВНОГО ТЕСТА С НЕВАЛИДНЫМ ЛОГИНОМ'


@pytest.fixture()
def invalid_password() -> str:
    return 'ЗАПУСК НЕГАТИВНОГО ТЕСТА С НЕВАЛИДНЫМ ПАРОЛЕМ'


@pytest.fixture()
def empty_fields_contact() -> str:
    return 'ЗАПУСК НЕГАТИВНОГО ТЕСТА С ПУСТЫМИ ПОЛЯМИ ФОРМЫ "CONTACT_US"'


@pytest.fixture()
def margin_height() -> str:
    return 'ЗАПУСК ПОЗИТИВНОГО ТЕСТА ДЛЯ ПРОВЕРКИ ВЫСОТЫ ПОЛЕЙ'


@pytest.fixture()
def login_button_color() -> str:
    return 'ЗАПУСК ПОЗИТИВНОГО ТЕСТА ДЛЯ ПРОВЕРКИ ЦВЕТА КНОПКИ ВХОДА'


@pytest.fixture()
def user_account() -> str:
    return 'ЗАПУСК ПОЗИТИВНОГО ТЕСТА ДЛЯ ПРОВЕРКИ ВХОДА ПОЛЬЗОВАТЕЛЯ В АККАУНТ'


@pytest.fixture()
def creating_a_post() -> str:
    return 'ЗАПУСК ПОЗИТИВНОГО ТЕСТА ДЛЯ ПРОВЕРКИ СОЗДАНИЯ ПОСТА ПО ПОЛЮ TITLE'


@pytest.fixture()
def contact_us_form() -> str:
    return 'ЗАПУСК ПОЗИТИВНОГО ТЕСТА ДЛЯ ПРОВЕРКИ ОТКРЫТИЯ ФОРМЫ "CONTACT_US"'


@pytest.fixture()
def filling_out_contact_us() -> str:
    return 'ЗАПУСК ПОЗИТИВНОГО ТЕСТА ДЛЯ ПРОВЕРКИ ЗАПОЛНЕНИЯ ФОРМЫ "CONTACT_US" И ОТПРАВКИ ДАННЫХ'


@pytest.fixture()
def expected_account_name() -> str:
    return f'Hello, {file_data["login_valid"]}'


@pytest.fixture()
def button_color_chrome() -> str:
    return 'rgba(255, 255, 255, 1)'


@pytest.fixture()
def button_color_firefox() -> str:
    return 'rgb(255, 255, 255)'


@pytest.fixture()
def field_height() -> str:
    return '56px'


@pytest.fixture()
def error_number() -> str:
    return '401'


@pytest.fixture()
def field_title():
    return 'Тестовый пост №5'


@pytest.fixture()
def field_description():
    return 'Описание тестового поста №5'


@pytest.fixture()
def field_content():
    return 'Создание пробного поста c помощью Selenium WebDriver Python'


@pytest.fixture()
def form_name() -> str:
    return 'Contact us!'


@pytest.fixture()
def your_name_field_contact_form() -> str:
    return file_data['login_valid']


@pytest.fixture()
def your_email_field_contact_form() -> str:
    return 'test@mail.ru'


@pytest.fixture()
def your_content_field_contact_form() -> str:
    return 'Тестовое заполнение формы "Contact_us"'


@pytest.fixture()
def verification_alert() -> str:
    return 'Form successfully submitted'
