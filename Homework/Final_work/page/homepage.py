import logging
import yaml
from selenium.webdriver.common.by import By
from .base_page import BasePage


with open('config.yaml') as file:
    file_data = yaml.safe_load(file)


class HomepageLocators:
    LOCATOR_ACCOUNT_NAME: tuple[str, str] = (By.XPATH, file_data['account_name'])
    LOCATOR_CREATE_NEW_POST: tuple[str, str] = (By.ID, file_data['button_create_new_post'])
    LOCATOR_CONTACT: tuple[str, str] = (By.XPATH, file_data['contact'])
    LOCATOR_BUTTON_LOGOUT: tuple[str, str] = (By.XPATH, file_data['button_logout'])


class HomepageHelper(BasePage):
    def account_name(self) -> str:
        logging.info('Проверка входа пользователя в личный кабинет')

        return self.find_element(HomepageLocators.LOCATOR_ACCOUNT_NAME).text

    def button_create_new_post(self) -> None:
        logging.info('Нажатие на кнопку создания поста')

        self.find_element(HomepageLocators.LOCATOR_CREATE_NEW_POST).click()

    def go_to_contact(self) -> str:
        logging.info('Проверка открытия формы "Contact_us"')

        return self.find_element(HomepageLocators.LOCATOR_CONTACT).click()

    def account_name_button(self) -> None:
        logging.info('Нажатие на кнопку имени пользователя "Hello, ..."')

        self.find_element(HomepageLocators.LOCATOR_ACCOUNT_NAME).click()

    def exit_personal_page(self) -> None:
        logging.info('Нажатие на кнопку "logout"')

        self.find_element(HomepageLocators.LOCATOR_BUTTON_LOGOUT).click()
