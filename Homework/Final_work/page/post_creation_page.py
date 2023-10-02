from typing import Any
from .base_page import BasePage
from .page_element_locators import PageElementLocators


class PostCreationPageHelper(BasePage):
    def __init__(self, driver: Any):
        super().__init__(driver)
        self.locators = PageElementLocators()

    def fill_title_field(self, title_text: str) -> None:
        self.entering_text_into_field(self.locators.get_locators()['LOCATOR_FIELD_TITLE'], title_text,
                                      description='"Поле ввода Title на странице создания постов Create Post"')

    def fill_description_field(self, description_text: str) -> None:
        self.entering_text_into_field(self.locators.get_locators()['LOCATOR_FIELD_DESCRIPTION'], description_text,
                                      description='"Поле ввода Description на странице создания постов Create Post"')

    def fill_content_field(self, content_text: str) -> None:
        self.entering_text_into_field(self.locators.get_locators()['LOCATOR_FIELD_CONTENT'], content_text,
                                      description='"Поле ввода Content на странице создания постов Create Post"')

    def save_post_button(self) -> None:
        self.click_on_element(self.locators.get_locators()['LOCATOR_SAVE_POST_BUTTON'],
                              description='на кнопку "SAVE" на странице создания постов Create Post')
