from testpage import OperationsHelper
import pytest
import logging


def test_1(initialize_web_driver):
    logging.info('Тест1 запуск')
    test_pag = OperationsHelper(initialize_web_driver)

    test_pag.go_to_site()
    test_pag.enter_login('test')
    test_pag.enter_password('test')
    test_pag.click_on_the_login_button()

    assert test_pag.checking_error_text() == '401'


if __name__ == '__main__':
    pytest.main(['-vv'])
