from pathlib import Path

BASE_URL = 'https://qa-desk.education-services.ru/api'

SIGNUP_URL = '/signup'
SIGNIN_URL = '/signin'
CREATE_LISTING_URL = '/create-listing'
UPDATE_LISTING_URL = '/update-offer'
DELETE_LISTING_URL = '/listings'
PROFILE_LISTINGS_URL = '/profile/listings'

REQUEST_TIMEOUT = 45

TEST_PASSWORD = 'TestPass123'
TEST_USER_NAME = 'Autotest User'

LISTING_CONDITION_NEW = 'Новый'
LISTING_CITY_MOSCOW = 'Москва'
LISTING_CATEGORY_AUTO = 'Авто'

BASE_LISTING_PAYLOAD = {
    'name': 'Autotest listing',
    'category': LISTING_CATEGORY_AUTO,
    'condition': LISTING_CONDITION_NEW,
    'city': LISTING_CITY_MOSCOW,
    'description': 'Autotest description',
    'price': '1000',
}

UPDATED_LISTING_NAME = 'Updated autotest listing'

DUPLICATE_EMAIL_MESSAGE = 'Почта уже используется'
DELETE_LISTING_SUCCESS_MESSAGE = 'Объявление удалено успешно'
UNAUTHORIZED_EDIT_MESSAGE = (
    'Оффер не найден или у вас нет прав на его редактирование'
)

PROJECT_ROOT = Path(__file__).resolve().parent
LISTING_IMAGE_PATH = PROJECT_ROOT / 'assets' / 'listing_image.jpg'
LISTING_IMAGE_MIME_TYPE = 'image/jpeg'
