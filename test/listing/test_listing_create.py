import allure

from data import BASE_LISTING_PAYLOAD


@allure.feature('Объявление')
@allure.story('Создание объявления')
class TestListingCreate:
    @allure.title('Успешное создание объявления в категории Авто')
    def test_listing_create_success(self, listing_client, registered_user):
        response = listing_client.create_listing(
            registered_user['token'],
            BASE_LISTING_PAYLOAD,
        )
        body = response.json()

        assert response.status_code == 201
        assert body['name'] == BASE_LISTING_PAYLOAD['name']
        assert body['category'] == BASE_LISTING_PAYLOAD['category']
        assert body['owner'] == registered_user['id']
