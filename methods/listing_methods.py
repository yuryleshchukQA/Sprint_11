import allure
import requests

from data import (
    BASE_URL,
    CREATE_LISTING_URL,
    DELETE_LISTING_URL,
    LISTING_IMAGE_MIME_TYPE,
    LISTING_IMAGE_PATH,
    PROFILE_LISTINGS_URL,
    REQUEST_TIMEOUT,
    UPDATE_LISTING_URL,
)


class ListingMethods:
    @staticmethod
    def _auth_headers(token):
        return {'Authorization': f'Bearer {token}'}

    @staticmethod
    def build_update_payload(listing, **field_updates):
        payload = {
            'name': listing['name'],
            'category': listing['category'],
            'condition': listing['condition'],
            'city': listing['city'],
            'description': listing['description'],
            'price': str(listing['price']),
        }
        payload.update(field_updates)
        payload['price'] = str(payload['price'])
        return payload

    @staticmethod
    def _build_image_files(image_path):
        image_bytes = image_path.read_bytes()
        filename = image_path.name
        return [
            ('images', (filename, image_bytes, LISTING_IMAGE_MIME_TYPE))
            for _ in range(3)
        ]

    @allure.step('Создание объявления')
    def create_listing(self, token, payload, image_path=LISTING_IMAGE_PATH):
        return requests.post(
            f'{BASE_URL}{CREATE_LISTING_URL}',
            data=payload,
            files=self._build_image_files(image_path),
            headers=self._auth_headers(token),
            timeout=REQUEST_TIMEOUT,
        )

    @allure.step('Редактирование объявления')
    def update_listing(self, token, listing_id, payload):
        form_data = {
            **payload,
            'img1': 'null',
            'img2': 'null',
            'img3': 'null',
        }
        return requests.patch(
            f'{BASE_URL}{UPDATE_LISTING_URL}/{listing_id}',
            data=form_data,
            headers=self._auth_headers(token),
            timeout=REQUEST_TIMEOUT,
        )

    @allure.step('Удаление объявления')
    def delete_listing(self, token, listing_id):
        return requests.delete(
            f'{BASE_URL}{DELETE_LISTING_URL}/{listing_id}',
            headers={
                **self._auth_headers(token),
                'Content-Type': 'application/json',
            },
            timeout=REQUEST_TIMEOUT,
        )

    @allure.step('Получить объявления пользователя')
    def get_own_listings(self, token, page=1):
        return requests.get(
            f'{BASE_URL}{PROFILE_LISTINGS_URL}/{page}',
            headers={
                **self._auth_headers(token),
                'Content-Type': 'application/json',
            },
            timeout=REQUEST_TIMEOUT,
        )

    @allure.step('Удалить все объявления пользователя')
    def delete_all_user_listings(self, token):
        response = self.get_own_listings(token)
        assert response.status_code == 200, response.text

        for listing in response.json()['offers']:
            self.delete_listing(token, listing['id'])
