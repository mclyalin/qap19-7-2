import pytest

from tests.utils import get_auth_data, parse
from tests.settings import token
from qap19_7_2.api import get_api_key, get_pets, delete_pet

@pytest.fixture(scope='session', autouse=True)
def session():
    email, password = get_auth_data(token)
    response = get_api_key(email, password)
    status, content, _ = parse(response)
    key = content['key']

    return status, key

    yield data

    response = parse(get_pets(key, filter=filter))
    pets = response['content']['pets']

    if not pets:
        return

    for pet in pets:
        id = pet.get('id')
        delete_pet(key, id)

