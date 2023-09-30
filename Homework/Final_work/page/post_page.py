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
        post_title = self.find_element(PostPageLocators.LOCATOR_TITLE_ON_THE_PAGE, time=2)
        post_text = post_title.text

        logging.info(f'Нахождение текста {post_text} в поле {PostPageLocators.LOCATOR_TITLE_ON_THE_PAGE[1]}')

        return post_text
