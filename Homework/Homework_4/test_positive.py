import time
from typing import Generator
import pytest
import yaml
import logging
from page.login_page import LoginPageHelper
from page.homepage import HomepageHelper
from page.post_creation_page import PostCreationPageHelper
from page.post_page import PostPageHelper
from page.contact_us_page import ContactUsHelper

with open('config.yaml') as file:
    file_data = yaml.safe_load(file)


def test_positive_input_field_height(initialize_web_driver: Generator, field_height: str) -> None:
    logging.info('Запуск позитивного теста для проверки высоты полей')

    login_page = LoginPageHelper(initialize_web_driver)
    login_page.go_to_site()
    result = login_page.input_field_height()

    try:
        login_page.save_screenshot_filename_in_directory(file_data['directory_screenshot'])
    except KeyError:
        error_message = ('Ошибка при обращении к наименованию директории в файле ".yaml". '
                         'Этот параметр не найден в файле конфигурации и не определен для сохранения скриншотов.')
        logging.exception(error_message)

    assert result == field_height, "Test_positive_input_field_height FAIL"


def test_positive_login_button_color(initialize_web_driver: Generator, button_color_chrome: str,
                                     button_color_firefox: str) -> None:
    logging.info('Запуск позитивного теста для проверки цвета кнопки входа')

    login_page = LoginPageHelper(initialize_web_driver)
    result = login_page.login_button_color()

    assert result == button_color_chrome or result == button_color_firefox, "Test_positive_login_button_color FAIL"


def test_positive_login_to_account(initialize_web_driver: Generator, expected_account_name: str) -> None:
    logging.info('Запуск позитивного теста для проверки входа пользователя в аккаунт')

    login_page = LoginPageHelper(initialize_web_driver)
    homepage = HomepageHelper(initialize_web_driver)

    login_page.enter_login(file_data['login_valid'])
    login_page.enter_password(file_data['password_valid'])
    login_page.click_on_the_login_button()
    result = homepage.account_name()
    time.sleep(2)

    try:
        login_page.save_screenshot_filename_in_directory(file_data['directory_screenshot'])
    except KeyError:
        error_message = ('Ошибка при обращении к наименованию директории в файле ".yaml". '
                         'Этот параметр не найден в файле конфигурации и не определен для сохранения скриншотов.')
        logging.exception(error_message)

    assert result == expected_account_name, "Test_positive_login_to_account FAIL"


def test_positive_adding_a_post(initialize_web_driver: Generator, field_title: str, field_description: str,
                                field_content: str):
    logging.info('Запуск позитивного теста для проверки создания поста по полю title')

    login_page = LoginPageHelper(initialize_web_driver)
    homepage = HomepageHelper(initialize_web_driver)
    post_creation_page = PostCreationPageHelper(initialize_web_driver)
    post_page = PostPageHelper(initialize_web_driver)

    time.sleep(1)
    homepage.button_create_new_post()
    time.sleep(1)

    post_creation_page.fill_title_field(field_title)
    post_creation_page.fill_description_field(field_description)
    post_creation_page.fill_content_field(field_content)
    post_creation_page.save_post_button()
    result = post_page.find_the_post_title_on_the_page()

    try:
        login_page.save_screenshot_filename_in_directory(file_data['directory_screenshot'])
    except KeyError:
        error_message = ('Ошибка при обращении к наименованию директории в файле ".yaml". '
                         'Этот параметр не найден в файле конфигурации и не определен для сохранения скриншотов.')
        logging.exception(error_message)

    assert field_title == result, "Test_positive_login_to_account FAIL"


def test_positive_opening_the_contact_us_form(initialize_web_driver: Generator, form_name: str) -> None:
    logging.info('Запуск позитивного теста для проверки открытия формы "Contact_us"')

    homepage = HomepageHelper(initialize_web_driver)
    contact_us_page = ContactUsHelper(initialize_web_driver)
    homepage.go_to_contact()
    time.sleep(1)
    resulting_page_title = contact_us_page.finding_the_form_title_text()

    try:
        homepage.save_screenshot_filename_in_directory(file_data['directory_screenshot'])
    except KeyError:
        error_message = ('Ошибка при обращении к наименованию директории в файле ".yaml". '
                         'Этот параметр не найден в файле конфигурации и не определен для сохранения скриншотов.')
        logging.exception(error_message)
    time.sleep(1)

    assert resulting_page_title == form_name, "Test_positive_opening_the_contact_us_form FAIL"


def test_positive_form_contact_us(initialize_web_driver: Generator, your_name_field_contact_form: str,
                                  your_email_field_contact_form: str, your_content_field_contact_form: str,
                                  verification_alert: str) -> None:
    logging.info('Запуск позитивного теста для проверки заполнения формы "Contact_us" и отправки данных')

    contact_us_page = ContactUsHelper(initialize_web_driver)
    contact_us_page.fill_your_name_field(your_name_field_contact_form)
    contact_us_page.fill_your_email_field(your_email_field_contact_form)
    contact_us_page.fill_your_content_field(your_content_field_contact_form)

    try:
        contact_us_page.save_screenshot_filename_in_directory(file_data['directory_screenshot'])
    except KeyError:
        error_message = ('Ошибка при обращении к наименованию директории в файле ".yaml". '
                         'Этот параметр не найден в файле конфигурации и не определен для сохранения скриншотов.')
        logging.exception(error_message)

    contact_us_page.click_on_the_contact_us_button()
    received_alert = contact_us_page.receiving_text_from_alert()

    assert received_alert == verification_alert, 'Test_positive_form_contact_us FAIL'


if __name__ == '__main__':
    pytest.main(['-vv'])
