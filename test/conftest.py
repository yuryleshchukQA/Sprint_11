import pytest

from data import BASE_LISTING_PAYLOAD, TEST_PASSWORD, TEST_USER_NAME
from generators.email_generator import generate_unique_email
from methods.listing_methods import ListingMethods
from methods.user_methods import UserMethods


def _make_signup_payload(name=TEST_USER_NAME):
    return {
        'email': generate_unique_email(),
        'password': TEST_PASSWORD,
        'name': name,
    }


def _register_user(user_client, name=TEST_USER_NAME):
    payload = _make_signup_payload(name)
    response = user_client.signup(payload)
    assert response.status_code == 201, response.text
    body = response.json()
    return {
        **payload,
        'id': body['user']['id'],
        'token': UserMethods.extract_signup_token(body),
    }


@pytest.fixture
def user_client():
    return UserMethods()


@pytest.fixture
def listing_client():
    return ListingMethods()


@pytest.fixture
def user_registration_payload():
    return _make_signup_payload()


@pytest.fixture
def user_already_registered(user_client):
    user_data = _register_user(user_client)
    yield {
        'email': user_data['email'],
        'password': user_data['password'],
        'name': user_data['name'],
    }


@pytest.fixture
def registered_user(user_client, listing_client):
    user_data = _register_user(user_client)
    yield user_data
    listing_client.delete_all_user_listings(user_data['token'])


@pytest.fixture
def created_listing(listing_client, registered_user):
    response = listing_client.create_listing(
        registered_user['token'],
        BASE_LISTING_PAYLOAD,
    )
    assert response.status_code == 201, response.text
    yield response.json()


@pytest.fixture
def listing_owned_by_other_user(user_client, listing_client):
    owner = _register_user(user_client, name='Owner User')
    other = _register_user(user_client, name='Other User')

    response = listing_client.create_listing(owner['token'], BASE_LISTING_PAYLOAD)
    assert response.status_code == 201, response.text
    listing = response.json()

    yield {
        'listing': listing,
        'other_token': other['token'],
    }

    listing_client.delete_listing(owner['token'], listing['id'])
