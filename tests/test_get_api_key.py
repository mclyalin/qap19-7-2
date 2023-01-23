import pytest
from tests.settings import data


email = {
  'blank': '',
  'invalid': 'test@user.com',
}

password = {
  'blank': '',
  'invalid': 'password',
}

def test_get_api_key(session):
    """Проверяем что запрос api ключа возвращает статус 200
    и в результате содержится key"""

    assert session['status'] == 200
    assert session['key']

# @pytest.mark.parametrize('key', [
#   'ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0ae729',
#   *data.values(),
# ], ids = [
#   'expired',
#   *data.keys(),
# ])
# def test_get_api_key_negative():
#     """Проверяем что запрос api ключа возвращает статус 400
#     и в результате не содержится key"""

#     pass
