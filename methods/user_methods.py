import allure
import requests

from data import BASE_URL, REQUEST_TIMEOUT, SIGNIN_URL, SIGNUP_URL


class UserMethods:
    HEADERS = {'Content-Type': 'application/json'}

    @staticmethod
    def extract_signup_token(response_body):
        return response_body['access_token']['access_token']

    @allure.step('Регистрация пользователя')
    def signup(self, payload):
        return requests.post(
            f'{BASE_URL}{SIGNUP_URL}',
            json=payload,
            headers=self.HEADERS,
            timeout=REQUEST_TIMEOUT,
        )

    @allure.step('Авторизация пользователя')
    def signin(self, email, password):
        return requests.post(
            f'{BASE_URL}{SIGNIN_URL}',
            json={'email': email, 'password': password},
            headers=self.HEADERS,
            timeout=REQUEST_TIMEOUT,
        )
