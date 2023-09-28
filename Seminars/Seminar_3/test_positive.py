from typing import Generator

import pytest
import yaml
import logging
from product_page import OperationsHelper

with open('config.yaml') as file:
    file_data = yaml.safe_load(file)


def test_positive_input_field_height(initialize_web_driver: Generator, field_height: str) -> None:
    logging.info('Запуск позитивного теста для проверки высоты полей')
    test_pag = OperationsHelper(initialize_web_driver)

    test_pag.go_to_site()
    result = test_pag.input_field_height()

    assert result == field_height, "Test_positive_input_field_height FAIL"


def test_positive_login_button_color(initialize_web_driver: Generator, button_color_chrome: str,
                                     button_color_firefox: str) -> None:
    logging.info('Запуск позитивного теста для проверки цвета кнопки входа')
    test_pag = OperationsHelper(initialize_web_driver)

    result = test_pag.login_button_color()

    assert result == button_color_chrome or result == button_color_firefox, "Test_positive_login_button_color FAIL"


def test_positive_login_to_account(initialize_web_driver: Generator, expected_account_name: str) -> None:
    logging.info('Запуск позитивного теста для проверки входа пользователя в аккаунт')
    test_pag = OperationsHelper(initialize_web_driver)

    test_pag.enter_login(file_data['login_valid'])
    test_pag.enter_password(file_data['password_valid'])
    test_pag.click_on_the_login_button()
    result = test_pag.account_name()

    test_pag.save_screenshot_filename_in_directory(file_data['directory_screenshot'])

    assert result == expected_account_name, "Test_positive_login_to_account FAIL"


if __name__ == '__main__':
    pytest.main(['-vv'])
