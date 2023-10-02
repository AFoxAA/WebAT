from typing import Any
from .base_page import BasePage
from .page_element_locators import PageElementLocators


class PostPageHelper(BasePage):
    def __init__(self, driver: Any):
        super().__init__(driver)
        self.locators = PageElementLocators()

    def find_the_post_title_on_the_page(self) -> str:
        return self.get_text_from_element(self.locators.get_locators()['LOCATOR_TITLE_ON_THE_PAGE'],
                                          description='по полю Title для проверки создания поста на странице поста')
