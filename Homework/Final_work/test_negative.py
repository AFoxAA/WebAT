import pytest
import time
import logging
import yaml
from typing import Generator
from Final_work import LoginPageHelper, HomepageHelper, ContactUsHelper, DirectoryNameError

with open('config.yaml') as file:
    file_data = yaml.safe_load(file)


def test_invalid_login(initialize_web_driver: Generator, error_number: str, invalid_login: str) -> None:
    logging.info(invalid_login)
    login_page = LoginPageHelper(initialize_web_driver)

    login_page.go_to_site()
    login_page.enter_login(file_data['login_invalid'])
    login_page.enter_password(file_data['password_valid'])
    login_page.click_on_the_login_button()
    time.sleep(2)

    try:
        login_page.save_screenshot_filename_in_directory(file_data['directory_screenshot'])
    except KeyError:
        error_message = DirectoryNameError()
        logging.exception(error_message)

    assert login_page.checking_error_text() == error_number, "Test_invalid_login FAIL"


def test_invalid_password(initialize_web_driver: Generator, error_number: str, invalid_password: str) -> None:
    logging.info(invalid_password)
    login_page = LoginPageHelper(initialize_web_driver)

    login_page.enter_login(file_data['login_valid'])
    login_page.enter_password(file_data['password_invalid'])
    login_page.click_on_the_login_button()
    time.sleep(2)

    try:
        login_page.save_screenshot_filename_in_directory(file_data['directory_screenshot'])
    except KeyError:
        error_message = DirectoryNameError()
        logging.exception(error_message)

    assert login_page.checking_error_text() == error_number, "Test_invalid_password FAIL"


def test_invalid_empty_fields_contact(initialize_web_driver: Generator, verification_alert: str,
                                      empty_fields_contact: str) -> None:
    logging.info(empty_fields_contact)

    login_page = LoginPageHelper(initialize_web_driver)
    homepage = HomepageHelper(initialize_web_driver)
    contact_us_page = ContactUsHelper(initialize_web_driver)

    login_page.enter_login(file_data['login_valid'])
    login_page.enter_password(file_data['password_valid'])
    login_page.click_on_the_login_button()

    homepage.go_to_contact()
    contact_us_page.click_on_the_contact_us_button()
    received_alert = contact_us_page.receiving_text_from_alert()

    homepage.account_name_button()
    homepage.exit_personal_page()

    assert received_alert == verification_alert, "Test_invalid_empty_fields_contact FAIL"


if __name__ == '__main__':
    pytest.main(['-vv'])
