import pytest
from tests.utils import parse, get_auth_data
from qap19_7_2.api import get_api_key


invalid_emails = {
  'blank': '',
  'invalid': 'test@user.com',
}

invalid_passwords = {
  'blank': '',
  'invalid': 'password',
}

def test_get_key(session):
    """Проверяем что запрос api ключа возвращает статус 200
    и в результате содержится key"""

    response = get_api_key(session['email'], session['password'])
    status, data, message = parse(response)
    assert status == 200, message
    assert 'key' in data
    key = data.get('key')
    assert key


# @pytest.mark.parametrize('key', [
#   'ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0ae729',
#   *data.values(),
# ], ids = [
#   'expired',
#   *data.keys(),
# ])
# def test_get_key_negative():
#     """Проверяем что запрос api ключа возвращает статус 400
#     и в результате не содержится key"""

#     pass
