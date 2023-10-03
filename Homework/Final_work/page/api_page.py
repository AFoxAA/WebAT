import logging
import requests
import yaml
from zeep import Client, Settings
from ..error_package import (ErrorReceivingToken, ErrorEntranceInvalidUrl,
                             InvalidUrlCreatePost, ErrorReceivingPostRequest)


class SoapAPI:
    def __init__(self, wsdl_url):
        self.settings = Settings(strict=False)
        self.client = Client(wsdl=wsdl_url, settings=self.settings)

    def check_text(self, text):
        return self.client.service.checkText(text)[0]['s']


class RestAPI:
    def __init__(self):
        with open('config.yaml', 'r') as f:
            self.config = yaml.safe_load(f)

        self.url_login = self.config['url_login']
        self.url_posts = self.config['url_posts']
        self.session = requests.Session()

    def login(self):
        logging.info('Получение токена для входа')
        try:
            response = requests.post(self.url_login, data={"username": self.config['login_valid'],
                                                           "password": self.config['password_valid']})
            if response.status_code == 200:
                return response.json().get("token")
            else:
                error_message = ErrorReceivingToken(response.status_code)
                logging.exception(error_message)
        except Exception:
            error_message = ErrorEntranceInvalidUrl(self.url_login)
            logging.exception(error_message)

    def create_post(self, token, data):
        logging.info('Отправка данных на сервер')
        try:
            url = self.url_posts
            headers = {"X-Auth-Token": token}
            response = self.session.post(url, headers=headers, json=data)
            return response
        except Exception:
            error_message = InvalidUrlCreatePost(self.url_login)
            logging.exception(error_message)

    def get_posts(self, token):
        logging.info('Получение данных с сервера')
        try:
            url = self.url_posts
            headers = {"X-Auth-Token": token}
            response = self.session.get(url, headers=headers)
            return response.json()["data"]
        except Exception:
            error_message = ErrorReceivingPostRequest()
            logging.exception(error_message)
