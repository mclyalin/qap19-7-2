import pytest

from tests.utils import get_auth_data
from tests.settings import token, filter, images
from qap19_7_2.api import PetFriends

@pytest.fixture(scope='session', autouse=True)
def session():
    email, password = get_auth_data(token)
    store = PetFriends()
    status, key = store.get_api_key(email, password)

    data = {
        'store': store,
        'status': status,
        'key': key,
        'filter': filter,
        'images': images,
    }

    yield data

    _, result = store.get_list_of_pets(key, filter=filter)
    pets = result.get('pets')

    if not pets:
        return

    for pet in pets:
        id = pet.get('id')
        store.delete_pet(key, id)

