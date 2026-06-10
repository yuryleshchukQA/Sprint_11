import allure

from data import DUPLICATE_EMAIL_MESSAGE


@allure.feature('Пользователь')
@allure.story('Регистрация пользователя')
class TestUserRegistration:
    @allure.title('Успешная регистрация нового пользователя с уникальным email')
    def test_user_registration_success(self, user_client, user_registration_payload):
        response = user_client.signup(user_registration_payload)
        body = response.json()

        assert response.status_code == 201
        assert body['user']['email'] == user_registration_payload['email']
        assert body['user']['name'] == user_registration_payload['name']
        assert 'access_token' in body['access_token']

    @allure.title('Повторная регистрация с уже существующим email — ошибка 400')
    def test_user_registration_duplicate_email(self, user_client, user_already_registered):
        response = user_client.signup(user_already_registered)

        assert response.status_code == 400
        assert response.json()['message'] == DUPLICATE_EMAIL_MESSAGE
