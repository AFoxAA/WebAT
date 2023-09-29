import os
import logging
import pytest
import yaml
from typing import Any
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open('config.yaml') as file:
    file_data: Any = yaml.safe_load(file)


class BasePage:
    def __init__(self, driver) -> None:
        self.driver: Any = driver
        self.base_url: Any = file_data['address']

    def find_element(self, locator, time=5) -> Any:
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        except Exception:
            error_message = (f'Элемент с локатором {locator} не найден после ожидания {time} секунд')
            logging.exception(error_message)

    def go_to_site(self) -> Any:
        try:
            return self.driver.get(self.base_url)
        except Exception:
            error_message = (f'Не удается получить доступ к сайту {self.base_url}. '
                             f'Пожалуйста, убедитесь в корректности URL.')
            logging.exception(error_message)
            pytest.fail(error_message, pytrace=False)

    def save_screenshot_filename_in_directory(self, directory: str) -> str:
        '''Сохранение скриншота в отдельной директории'''
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)

            current_datetime: datetime = datetime.now()
            formatted_datetime: str = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
            capture_path: str = os.path.join(directory, f"{formatted_datetime}.png")

            self.driver.save_screenshot(capture_path)

            return capture_path
        except Exception:
            error_message = f'Ошибка при сохранении скриншота'
            logging.exception(error_message)
