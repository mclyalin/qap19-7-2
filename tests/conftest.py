import pytest

from utils.utils import get_auth_data, parse
from tests.settings import token, filter, images
from qap19_7_2.api import get_api_key, get_pets, delete_pet

@pytest.fixture(scope='session', autouse=True)
def session():
    email, password = get_auth_data(token)
    response = parse(get_api_key(email, password))

    status = response['status']
    key = response['content']['key']

    data = {
        'status': status,
        'key': key,
        'filter': filter,
        'images': images,
    }

    yield data

    response = parse(get_pets(key, filter=filter))
    pets = response['content']['pets']

    if not pets:
        return

    for pet in pets:
        id = pet.get('id')
        delete_pet(key, id)

