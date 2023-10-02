from typing import Any
from .base_page import BasePage
from .page_element_locators import PageElementLocators


class HomepageHelper(BasePage):
    def __init__(self, driver: Any):
        super().__init__(driver)
        self.locators = PageElementLocators()

    def account_name(self) -> str:
        return self.get_text_from_element(self.locators.get_locators()['LOCATOR_ACCOUNT_NAME'],
                                          description='для проверки входа пользователя в личный кабинет')

    def button_create_new_post(self) -> None:
        self.click_on_element(self.locators.get_locators()['LOCATOR_CREATE_NEW_POST'],
                              description='на кнопку "Create new post" на домашней странице')

    def go_to_contact(self) -> None:
        self.click_on_element(self.locators.get_locators()['LOCATOR_CONTACT'],
                              description='на кнопку "Contact" на домашней странице для открытия формы "Contact_us"')

    def account_name_button(self) -> None:
        self.click_on_element(self.locators.get_locators()['LOCATOR_ACCOUNT_NAME'],
                              description='на кнопку имени пользователя "Hello, ..." на домашней странице')

    def exit_personal_page(self) -> None:
        self.click_on_element(self.locators.get_locators()['LOCATOR_BUTTON_LOGOUT'],
                              description='на кнопку "logout" в выпадающем меню  "Hello, ..." на домашней странице')
