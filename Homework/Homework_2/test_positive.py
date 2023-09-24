import os
import time

import yaml
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from module_site_automation import Site
import pytest

with open('config.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)

site = Site(data['address'], data['sleep'], data['browser'])


def test_positive_input_field_height(field_height):
    result = site.driver.find_element(By.CSS_SELECTOR, data['input_field_height']).value_of_css_property('height')

    assert result == field_height, "test_positive_input_field_height FAIL"


def test_positive_login_button_color(button_color_chrome, button_color_firefox):
    result = site.driver.find_element(By.XPATH, data['login_button_color']).value_of_css_property('color')

    assert result == button_color_chrome or button_color_firefox, "test_positive_login_button_color FAIL"


def test_positive_login_to_account(expected_account_name):
    load_dotenv()

    site.driver.find_element(By.XPATH, data['username']).send_keys(data['login_valid'])
    site.driver.find_element(By.XPATH, data['password']).send_keys(os.getenv('password'))
    site.driver.find_element(By.XPATH, data['button_login']).click()
    result = site.driver.find_element(By.XPATH, data['account_name']).text

    site.save_screenshot_filename_in_directory(data['directory_screenshot'])

    assert result == expected_account_name, "test_positive_login_to_account FAIL"


def test_positive_adding_a_post(field_title, field_description, field_content):
    time.sleep(1)
    site.driver.find_element(By.ID, data['button_create_new_post']).click()
    time.sleep(1)

    site.driver.find_element(By.XPATH, data['field_title']).send_keys(field_title)
    site.driver.find_element(By.XPATH, data['field_description']).send_keys(field_description)
    site.driver.find_element(By.XPATH, data['field_content']).send_keys(field_content)
    site.driver.find_element(By.XPATH, data['save_post_button']).click()

    result = site.driver.find_element(By.CSS_SELECTOR, data['post_titles_on_the_page']).text

    site.save_screenshot_filename_in_directory(data['directory_screenshot'])
    site.close()

    assert field_title == result, "test_positive_login_to_account FAIL"


if __name__ == '__main__':
    pytest.main(['-vv'])
