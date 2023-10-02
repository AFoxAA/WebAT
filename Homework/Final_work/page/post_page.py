from .base_page import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

with open('config.yaml') as file:
    file_data = yaml.safe_load(file)


class PostPageLocators:
    LOCATOR_TITLE_ON_THE_PAGE: tuple[str, str] = (By.CSS_SELECTOR, file_data['title_on_the_page'])


class PostPageHelper(BasePage):
    def find_the_post_title_on_the_page(self) -> str:
        return self.get_text_from_element(PostPageLocators.LOCATOR_TITLE_ON_THE_PAGE,
                                          description='по полю Title для проверки создания поста на странице поста')
