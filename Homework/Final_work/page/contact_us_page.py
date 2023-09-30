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
        logging.info(f'Отправлять имя элементу {ContactUsPageLocators.LOCATOR_FIELD_YOUR_NAME[1]}')

        self.find_element(ContactUsPageLocators.LOCATOR_FIELD_YOUR_NAME).send_keys(text_your_name)

    def fill_your_email_field(self, text_your_email: str) -> None:
        logging.info(f'Отправлять email элементу {ContactUsPageLocators.LOCATOR_FIELD_YOUR_NAME[1]}')

        self.find_element(ContactUsPageLocators.LOCATOR_FIELD_YOUR_EMAIL).send_keys(text_your_email)

    def fill_your_content_field(self, text_content: str) -> None:
        logging.info(f'Отправлять content элементу {ContactUsPageLocators.LOCATOR_FIELD_YOUR_CONTENT[1]}')

        self.find_element(ContactUsPageLocators.LOCATOR_FIELD_YOUR_CONTENT).send_keys(text_content)

    def click_on_the_contact_us_button(self):
        logging.info('Нажатие кнопки "CONTACT US"')

        self.find_element(ContactUsPageLocators.LOCATOR_CONTACT_US_BUTTON).click()

    def receiving_text_from_alert(self):
        logging.info('Получаем текст из alert')

        time.sleep(2)
        alert = self.driver.switch_to.alert
        result = alert.text

        logging.info('Закрываем alert')
        alert.accept()

        return result
