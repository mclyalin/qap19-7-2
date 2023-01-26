import pytest

from tests.utils import get_auth_data, parse
from tests.settings import token
from qap19_7_2.api import get_api_key, get_pets, delete_pet

@pytest.fixture(scope='session', autouse=True)
def session():
    email, password = get_auth_data(token)

    data = {
      'email': email,
      'password': password,
    }

    return data


