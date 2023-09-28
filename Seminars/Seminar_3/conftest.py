from typing import Any, Generator
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('config.yaml', encoding='utf-8') as file:
    file_data: Any = yaml.safe_load(file)
    browser: Any = file_data['browser']


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

    yield driver

    driver.quit()


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
