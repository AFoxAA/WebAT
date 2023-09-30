import logging
import yaml
from selenium.webdriver.common.by import By
from .base_page import BasePage

with open('config.yaml') as file:
    file_data = yaml.safe_load(file)


class LoginPageLocators:
    LOCATOR_LOGIN_FIELD: tuple[str, str] = (By.XPATH, file_data['username'])
    LOCATOR_PASSWORD_FIELD: tuple[str, str] = (By.XPATH, file_data['password'])
    LOCATOR_BUTTON_LOGIN: tuple[str, str] = (By.CSS_SELECTOR, file_data['button_login'])
    LOCATOR_ERROR_MESSAGE: tuple[str, str] = (By.XPATH, file_data['error'])
    LOCATOR_INPUT_FIELD_HEIGHT: tuple[str, str] = (By.CSS_SELECTOR, file_data['input_field_height'])
    LOCATOR_LOGIN_BUTTON_COLOR: tuple[str, str] = (By.XPATH, file_data['login_button_color'])


class LoginPageHelper(BasePage):
    def enter_login(self, login: str) -> None:
        logging.info(f'Отправлять логин элементу {LoginPageLocators.LOCATOR_LOGIN_FIELD[1]}')

        login_field = self.find_element(LoginPageLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(login)

    def enter_password(self, password: str) -> None:
        logging.info(f'Отправлять пароль элементу {LoginPageLocators.LOCATOR_PASSWORD_FIELD[1]}')

        login_field = self.find_element(LoginPageLocators.LOCATOR_PASSWORD_FIELD)
        login_field.clear()
        login_field.send_keys(password)

    def click_on_the_login_button(self) -> None:
        logging.info('Нажатие кнопки входа в личный кабинет пользователя')

        self.find_element(LoginPageLocators.LOCATOR_BUTTON_LOGIN).click()

    def checking_error_text(self) -> str:
        error_massage = self.find_element(LoginPageLocators.LOCATOR_ERROR_MESSAGE, time=2)
        text_error = error_massage.text

        logging.info(f'Нахождение текста {text_error} в поле ошибки {LoginPageLocators.LOCATOR_ERROR_MESSAGE[1]}')

        return text_error

    def input_field_height(self) -> str:
        logging.info('Проверка высоты полей логина и пароля')

        field_height = self.find_element(LoginPageLocators.LOCATOR_INPUT_FIELD_HEIGHT)
        result = field_height.value_of_css_property('height')

        return result

    def login_button_color(self) -> str:
        logging.info('Проверка цвета кнопки входа в личный кабинет пользователя')

        button_color = self.find_element(LoginPageLocators.LOCATOR_LOGIN_BUTTON_COLOR)
        result = button_color.value_of_css_property('color')

        return result
