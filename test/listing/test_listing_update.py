import allure

from data import UNAUTHORIZED_EDIT_MESSAGE, UPDATED_LISTING_NAME


@allure.feature('Объявление')
@allure.story('Редактирование объявления')
class TestListingUpdate:
    @allure.title('Успешное редактирование названия объявления')
    def test_listing_update_name_success(
        self,
        listing_client,
        registered_user,
        created_listing,
    ):
        update_payload = listing_client.build_update_payload(
            created_listing,
            name=UPDATED_LISTING_NAME,
        )
        response = listing_client.update_listing(
            registered_user['token'],
            created_listing['id'],
            update_payload,
        )

        assert response.status_code == 200
        assert response.json()['name'] == UPDATED_LISTING_NAME

    @allure.title(
        'Редактирование чужого объявления под токеном другого пользователя — ошибка 401'
    )
    def test_listing_update_by_other_user_unauthorized(
        self,
        listing_client,
        listing_owned_by_other_user,
    ):
        update_payload = listing_client.build_update_payload(
            listing_owned_by_other_user['listing'],
            name=UPDATED_LISTING_NAME,
        )
        response = listing_client.update_listing(
            listing_owned_by_other_user['other_token'],
            listing_owned_by_other_user['listing']['id'],
            update_payload,
        )

        assert response.status_code == 401
        assert response.json()['message'] == UNAUTHORIZED_EDIT_MESSAGE
