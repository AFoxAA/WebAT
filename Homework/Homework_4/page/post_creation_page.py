from .base_page import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

with open('config.yaml') as file:
    file_data = yaml.safe_load(file)


class PostCreationLocators:
    LOCATOR_FIELD_TITLE: tuple[str, str] = (By.XPATH, file_data['field_title'])
    LOCATOR_FIELD_DESCRIPTION: tuple[str, str] = (By.XPATH, file_data['field_description'])
    LOCATOR_FIELD_CONTENT: tuple[str, str] = (By.XPATH, file_data['field_content'])
    LOCATOR_SAVE_POST_BUTTON: tuple[str, str] = (By.XPATH, file_data['save_post_button'])


class PostCreationPageHelper(BasePage):
    def fill_title_field(self, title_text: str) -> None:
        logging.info('Добавление информации в поле title')

        self.find_element(PostCreationLocators.LOCATOR_FIELD_TITLE).send_keys(title_text)

    def fill_description_field(self, description_text: str) -> None:
        logging.info('Добавление информации в поле description')

        self.find_element(PostCreationLocators.LOCATOR_FIELD_DESCRIPTION).send_keys(description_text)

    def fill_content_field(self, content_text: str) -> None:
        logging.info('Добавление информации в поле content')

        self.find_element(PostCreationLocators.LOCATOR_FIELD_CONTENT).send_keys(content_text)

    def save_post_button(self) -> None:
        logging.info('Нажатие кнопки сохранения поста')

        self.find_element(PostCreationLocators.LOCATOR_SAVE_POST_BUTTON).click()
