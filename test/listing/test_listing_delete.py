import allure

from data import DELETE_LISTING_SUCCESS_MESSAGE


@allure.feature('Объявление')
@allure.story('Удаление объявления')
class TestListingDelete:
    @allure.title('Успешное удаление объявления')
    def test_listing_delete_success(self, listing_client, registered_user, created_listing):
        response = listing_client.delete_listing(
            registered_user['token'],
            created_listing['id'],
        )

        assert response.status_code == 200
        assert response.json()['message'] == DELETE_LISTING_SUCCESS_MESSAGE
