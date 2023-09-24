import os
import yaml
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from module_site_automation import Site
import pytest

with open('config.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)

site = Site(data['address'], data['sleep'], data['browser'])


def test_negative_login_to_account(error_number):
    load_dotenv()

    site.driver.find_element(By.XPATH, data['username']).send_keys(data['login_invalid'])
    site.driver.find_element(By.XPATH, data['password']).send_keys(os.getenv('password'))
    site.driver.find_element(By.XPATH, data['button_login']).click()
    result = site.driver.find_element(By.XPATH, data['error']).text
    print(result)

    site.save_screenshot_filename_in_directory(data['directory_screenshot'])

    site.driver.find_element(By.XPATH, data['username']).clear()
    site.driver.find_element(By.XPATH, data['password']).clear()
    site.close()
    assert result == error_number, "test_step3 FAIL"


if __name__ == '__main__':
    pytest.main(['-vv'])
