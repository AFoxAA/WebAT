import os
import logging
import time
import pytest
import yaml
from typing import Any
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..error_package import *

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
            error_message = LocatorError(locator, time)
            logging.exception(error_message)

    def go_to_site(self) -> Any:
        try:
            return self.driver.get(self.base_url)
        except Exception:
            error_message = SiteAccessError(self.base_url)
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
            error_message = ErrorWhenSavingScreenshot()
            logging.exception(error_message)

    def entering_text_into_field(self, locator: Any, word: Any, description=None) -> bool:
        element_name: Any = description if description else locator

        logging.debug(f'Отправить текст: "{word}", элементу: {element_name}')
        field = self.find_element(locator)

        try:
            field.send_keys(word) if not field.get_attribute("value") else (field.clear(), field.send_keys(word))

        except:
            error_message = TextInputError(locator, word)
            logging.exception(error_message)
            return False
        return True

    def click_on_element(self, locator: Any, description=None):
        element_name: Any = description if description else locator
        find_element = self.find_element(locator)
        if not find_element:
            return False
        try:
            find_element.click()
        except:
            error_message = ErrorWhenClicking()
            logging.exception(error_message)
            return False
        logging.debug(f'Клик {element_name}')
        return True

    def get_text_from_element(self, locator: Any, description=None) -> Any | None:
        element_name: Any = description if description else locator
        find_field: Any = self.find_element(locator, time=5)
        if not find_field:
            return None
        try:
            get_text = find_field.text
        except:
            error_message = ErrorReceivingText(element_name)
            logging.exception(error_message)
            return None
        logging.debug(f'Получен текст "{get_text}" {element_name}')
        return get_text

    def check_color_and_height_element(self, locator: Any, parameter: str, description=None) -> str:
        element_name: Any = description if description else locator
        get_element: Any = self.find_element(locator)
        result = get_element.value_of_css_property(parameter)
        logging.debug(f'Проверка {element_name}')
        return result

    def receiving_text_from_alert(self) -> str | None:
        try:
            logging.info('Получаем текст из alert')

            time.sleep(2)
            alert: Any = self.driver.switch_to.alert
            result: str = alert.text

            logging.info('Закрываем alert')
            alert.accept()

            return result
        except Exception:
            error_message = AlertError()
            logging.exception(error_message)
            return None
