import logging
import pytest
from Final_work import RestAPI, ErrorApi


def test_positive_rest_api_create_post(test_data, post_presence_by_description, post_creation_check):
    logging.info(post_creation_check)
    api_client = RestAPI()

    token = api_client.login()

    api_client.create_post(token, test_data)
    posts = api_client.get_posts(token)
    try:
        assert post_presence_by_description in [i["description"] for i in posts], \
            f'Слово/Выражение "{post_presence_by_description}" не найдено в списке предложенных'
    except Exception as e:
        error_message = ErrorApi()
        logging.exception(f"{error_message}: {e}")
        raise


def test_positive_soap_api_check_text(api_page, valid_word, invalid_word, checking_correct_word):
    logging.info(checking_correct_word)
    result = valid_word
    try:
        assert result in api_page.check_text(invalid_word), f'"Слово {result} не найдено в списке предложенных"'
    except Exception as e:
        error_message = ErrorApi()
        logging.exception(f"{error_message}: {e}")
        raise


if __name__ == '__main__':
    pytest.main(['-vv'])
