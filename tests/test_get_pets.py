import pytest


def test_get_pets(session):
    """Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этот ключ
    запрашиваем список всех питомцев и проверяем что список не пустой"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_pets(auth_key)

    assert status == 200
    assert 'pets' in result
    assert len(result['pets']) > 0