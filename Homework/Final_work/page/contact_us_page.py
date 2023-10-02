from typing import Any
from .base_page import BasePage
from .page_element_locators import PageElementLocators


class ContactUsHelper(BasePage):
    def __init__(self, driver: Any):
        super().__init__(driver)
        self.locators = PageElementLocators()

    def finding_the_form_title_text(self) -> str:
        return self.get_text_from_element(self.locators.get_locators()['LOCATOR_FORM_NAME'], description='в заголовке формы')

    def fill_your_name_field(self, text_your_name: str):
        self.entering_text_into_field(self.locators.get_locators()['LOCATOR_FIELD_YOUR_NAME'], text_your_name,
                                      description='"Поле ввода Your name на странице Contact us!"')

    def fill_your_email_field(self, text_your_email: str) -> None:
        self.entering_text_into_field(self.locators.get_locators()['LOCATOR_FIELD_YOUR_EMAIL'], text_your_email,
                                      description='"Поле ввода Your email на странице Contact us!"')

    def fill_your_content_field(self, text_content: str) -> None:
        self.entering_text_into_field(self.locators.get_locators()['LOCATOR_FIELD_YOUR_CONTENT'], text_content,
                                      description='"Поле ввода Content на странице Contact us!"')

    def click_on_the_contact_us_button(self):
        self.click_on_element(self.locators.get_locators()['LOCATOR_CONTACT_US_BUTTON'], description='на кнопку "CONTACT US"')
