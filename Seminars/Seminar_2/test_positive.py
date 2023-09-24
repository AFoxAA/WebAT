import os
import yaml
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from module_site_automation import Site
import pytest

with open('config.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)

site = Site(data['address'], data['sleep'], data['browser'])


def test_step_positive1(field_height):
    result = site.driver.find_element(By.CSS_SELECTOR, data['input_field_height']).value_of_css_property('height')

    assert result == field_height, "test_step_positive1 FAIL"


def test_step_positive2(button_color_chrome, button_color_firefox):
    result = site.driver.find_element(By.XPATH, data['login_button_color']).value_of_css_property('color')

    assert result == button_color_chrome or button_color_firefox, "test_step_positive2 FAIL"


def test_step_positive3(elem_login, elem_password, elem_button_login, account_name, expected_account_name):
    load_dotenv()

    site.driver.find_element(By.XPATH, elem_login).send_keys(data['login_valid'])
    site.driver.find_element(By.XPATH, elem_password).send_keys(os.getenv('password'))
    site.driver.find_element(By.XPATH, elem_button_login).click()
    result = site.driver.find_element(By.XPATH, account_name).text

    site.save_screenshot_filename_in_directory(data['directory_screenshot'])
    site.close()

    assert result == expected_account_name, "test_step3 FAIL"


if __name__ == '__main__':
    pytest.main(['-vv'])
