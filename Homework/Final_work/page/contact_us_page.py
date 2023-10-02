import time
import logging
import yaml
from selenium.webdriver.common.by import By
from .base_page import BasePage

with open('config.yaml') as file:
    file_data = yaml.safe_load(file)


class ContactUsPageLocators:
    LOCATOR_FORM_NAME: tuple[str, str] = (By.XPATH, file_data['form_name'])
    LOCATOR_FIELD_YOUR_NAME: tuple[str, str] = (By.XPATH, file_data['field_your_name'])
    LOCATOR_FIELD_YOUR_EMAIL: tuple[str, str] = (By.XPATH, file_data['field_your_email'])
    LOCATOR_FIELD_YOUR_CONTENT: tuple[str, str] = (By.XPATH, file_data['field_your_content'])
    LOCATOR_CONTACT_US_BUTTON: tuple[str, str] = (By.XPATH, file_data['contact_us_button'])


class ContactUsHelper(BasePage):
    def finding_the_form_title_text(self) -> str:
        form_name = self.find_element(ContactUsPageLocators.LOCATOR_FORM_NAME, time=2).text

        logging.info(f'Нахождение текста "{form_name}" в поле {ContactUsPageLocators.LOCATOR_FORM_NAME[1]}')

        return form_name

    def fill_your_name_field(self, text_your_name: str):
        self.entering_text_into_field(ContactUsPageLocators.LOCATOR_FIELD_YOUR_NAME, text_your_name,
                                      description='"Поле ввода Your name на странице Contact us!"')

    def fill_your_email_field(self, text_your_email: str) -> None:
        self.entering_text_into_field(ContactUsPageLocators.LOCATOR_FIELD_YOUR_EMAIL, text_your_email,
                                      description='"Поле ввода Your email на странице Contact us!"')

    def fill_your_content_field(self, text_content: str) -> None:
        self.entering_text_into_field(ContactUsPageLocators.LOCATOR_FIELD_YOUR_CONTENT, text_content,
                                      description='"Поле ввода Content на странице Contact us!"')

    def click_on_the_contact_us_button(self):
        self.click_on_element(ContactUsPageLocators.LOCATOR_CONTACT_US_BUTTON, description='на кнопку "CONTACT US"')
