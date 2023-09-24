import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime


class Site:
    def __init__(self, address_site, sleep, browser) -> None:
        if browser == 'firefox':
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')
            self.driver = webdriver.Firefox(service=service, options=options)

        elif browser == 'chrome':
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            self.driver = webdriver.Chrome(service=service, options=options)

        self.driver.implicitly_wait(sleep)
        self.driver.maximize_window()
        self.driver.get(address_site)

    def save_screenshot_filename_in_directory(self, directory: str) -> str:
        '''Сохранение скриншота в отдельной директории'''

        # Создание папки, если она не существует
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Создание уникального имени файла скриншота
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        capture_path = os.path.join(directory, f"{formatted_datetime}.png")

        # Сохранение скриншота
        self.driver.save_screenshot(capture_path)

        return capture_path

    def close(self) -> None:
        self.driver.close()
