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
        self.entering_text_into_field(LoginPageLocators.LOCATOR_LOGIN_FIELD, login,
                                      description='"Поле ввода логина на странице авторизации"')

    def enter_password(self, password: str) -> None:
        self.entering_text_into_field(LoginPageLocators.LOCATOR_PASSWORD_FIELD, password,
                                      description='"Поле ввода password на странице авторизации"')

    def click_on_the_login_button(self) -> None:
        self.click_on_element(LoginPageLocators.LOCATOR_BUTTON_LOGIN,
                              description='на кнопку "Login" на странице авторизации')

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
