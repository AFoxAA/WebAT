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
        self.entering_text_into_field(PostCreationLocators.LOCATOR_FIELD_TITLE, title_text,
                                      description='"Поле ввода Title на странице создания постов Create Post"')

    def fill_description_field(self, description_text: str) -> None:
        self.entering_text_into_field(PostCreationLocators.LOCATOR_FIELD_DESCRIPTION, description_text,
                                      description='"Поле ввода Description на странице создания постов Create Post"')

    def fill_content_field(self, content_text: str) -> None:
        self.entering_text_into_field(PostCreationLocators.LOCATOR_FIELD_CONTENT, content_text,
                                      description='"Поле ввода Content на странице создания постов Create Post"')

    def save_post_button(self) -> None:
        self.click_on_element(PostCreationLocators.LOCATOR_SAVE_POST_BUTTON,
                              description='на кнопку "SAVE" на странице создания постов Create Post')
