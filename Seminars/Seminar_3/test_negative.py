import time
from typing import Generator
from product_page import OperationsHelper
import pytest
import logging
import yaml

with open('config.yaml') as file:
    file_data = yaml.safe_load(file)


def test_invalid_login(initialize_web_driver: Generator, error_number: str) -> None:
    logging.info('Запуск негативного теста с невалидным логином')
    test_pag = OperationsHelper(initialize_web_driver)

    test_pag.go_to_site()
    test_pag.enter_login(file_data['login_invalid'])
    test_pag.enter_password(file_data['password_valid'])
    test_pag.click_on_the_login_button()
    time.sleep(2)

    test_pag.save_screenshot_filename_in_directory(file_data['directory_screenshot'])

    assert test_pag.checking_error_text() == error_number


def test_invalid_password(initialize_web_driver: Generator, error_number: str) -> None:
    logging.info('Запуск негативного теста с невалидным паролем')
    test_pag = OperationsHelper(initialize_web_driver)

    test_pag.enter_login(file_data['login_valid'])
    test_pag.enter_password(file_data['password_invalid'])
    test_pag.click_on_the_login_button()
    time.sleep(2)

    test_pag.save_screenshot_filename_in_directory(file_data['directory_screenshot'])

    assert test_pag.checking_error_text() == error_number


def test_invalid_password_and_login(initialize_web_driver: Generator, error_number: str) -> None:
    logging.info('Запуск негативного теста с невалидным паролем')
    test_pag = OperationsHelper(initialize_web_driver)

    test_pag.enter_login(file_data['login_invalid'])
    test_pag.enter_password(file_data['password_invalid'])
    test_pag.click_on_the_login_button()
    time.sleep(2)

    test_pag.save_screenshot_filename_in_directory(file_data['directory_screenshot'])

    assert test_pag.checking_error_text() == error_number


if __name__ == '__main__':
    pytest.main(['-vv'])
