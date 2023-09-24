import os
import yaml
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from module_site_automation import Site
import pytest

with open('config.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)

site = Site(data['address'], data['sleep'], data['browser'])


def test_step_negative(elem_login, elem_password, elem_button_login, logging_error, error_number):
    load_dotenv()

    site.driver.find_element(By.XPATH, elem_login).send_keys(data['login_invalid'])
    site.driver.find_element(By.XPATH, elem_password).send_keys(os.getenv('password'))
    site.driver.find_element(By.XPATH, elem_button_login).click()
    result = site.driver.find_element(By.XPATH, logging_error).text

    site.save_screenshot_filename_in_directory(data['directory_screenshot'])

    site.driver.find_element(By.XPATH, elem_login).clear()
    site.driver.find_element(By.XPATH, elem_password).clear()
    site.close()
    assert result == error_number, "test_step3 FAIL"


if __name__ == '__main__':
    pytest.main(['-vv'])
