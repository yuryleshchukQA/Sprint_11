import allure


@allure.feature('Пользователь')
@allure.story('Авторизация пользователя')
class TestUserLogin:
    @allure.title('Успешная авторизация ранее зарегистрированного пользователя')
    def test_user_login_success(self, user_client, registered_user):
        response = user_client.signin(
            registered_user['email'],
            registered_user['password'],
        )
        body = response.json()

        assert response.status_code == 201
        assert body['user']['email'] == registered_user['email']
        assert body['user']['id'] == registered_user['id']
        assert 'access_token' in body['token']
