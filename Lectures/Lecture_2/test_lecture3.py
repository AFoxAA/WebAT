import os
import time
import pytest
import yaml
from module_site_automation import TestSite
from dotenv import load_dotenv

with open('config.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)

site = TestSite(data['address'], data['sleep'], data['browser'])


def test_step3() -> None:
    load_dotenv()
    initial_url = site.driver.current_url

    site.find_element('xpath', data['username']).send_keys(os.getenv('login'))
    site.find_element('xpath', data['password']).send_keys(os.getenv('password'))
    site.find_element('xpath', data['button_login']).click()
    time.sleep(2)

    new_url = site.driver.current_url
    site.save_screenshot_filename_in_directory(data['directory_screenshot'])

    site.close()
    assert initial_url != new_url, f"test_step3 FAIL"


if __name__ == '__main__':
    pytest.main(['-vv'])
