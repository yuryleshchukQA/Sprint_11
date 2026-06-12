from data import TEST_PASSWORD, TEST_USER_NAME
from generators.email_generator import generate_unique_email
from methods.user_methods import UserMethods


def make_signup_payload(name=TEST_USER_NAME):
    return {
        'email': generate_unique_email(),
        'password': TEST_PASSWORD,
        'name': name,
    }


def register_user(user_client, name=TEST_USER_NAME):
    payload = make_signup_payload(name)
    response = user_client.signup(payload)
    body = response.json()
    return {
        **payload,
        'id': body['user']['id'],
        'token': UserMethods.extract_signup_token(body),
    }
