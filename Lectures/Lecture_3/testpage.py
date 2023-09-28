from Base_Page import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    LOCATOR_PASSWORD_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_BUTTON_LOGIN = (By.CSS_SELECTOR, 'button')
    LOCATOR_ERROR_MESSAGE = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')


class OperationsHelper(BasePage):
    def enter_login(self, login):
        logging.info(f'Отправлять {login} элементу {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()

        login_field.send_keys(login)

    def enter_password(self, password):
        logging.info(f'Отправлять {password} элементу {TestSearchLocators.LOCATOR_PASSWORD_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASSWORD_FIELD)
        login_field.clear()

        login_field.send_keys(password)

    def click_on_the_login_button(self):
        logging.info('Нажатие кнопки входа')
        self.find_element(TestSearchLocators.LOCATOR_BUTTON_LOGIN).click()

    def checking_error_text(self):
        error_massage = self.find_element(TestSearchLocators.LOCATOR_ERROR_MESSAGE, time=3)
        text = error_massage.text
        logging.info(f'Нахождение текста {text} в поле ошибки {TestSearchLocators.LOCATOR_ERROR_MESSAGE[1]}')
        return text





