import pytest

from helpers.listing_helper import (
    create_listing,
    delete_all_user_listings,
    delete_listing,
)
from helpers.user_helper import register_user
from methods.listing_methods import ListingMethods
from methods.user_methods import UserMethods


@pytest.fixture
def user_client():
    return UserMethods()


@pytest.fixture
def listing_client():
    return ListingMethods()


@pytest.fixture
def user_already_registered(user_client):
    user_data = register_user(user_client)
    return {
        'email': user_data['email'],
        'password': user_data['password'],
        'name': user_data['name'],
    }


@pytest.fixture
def registered_user(user_client, listing_client):
    user_data = register_user(user_client)
    yield user_data
    delete_all_user_listings(listing_client, user_data['token'])


@pytest.fixture
def created_listing(listing_client, registered_user):
    return create_listing(listing_client, registered_user['token'])


@pytest.fixture
def listing_owned_by_other_user(user_client, listing_client):
    owner = register_user(user_client, name='Owner User')
    other = register_user(user_client, name='Other User')
    listing = create_listing(listing_client, owner['token'])

    yield {
        'listing': listing,
        'other_token': other['token'],
    }

    delete_listing(listing_client, owner['token'], listing['id'])
