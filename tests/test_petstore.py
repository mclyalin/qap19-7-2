import pytest
import os


def test_get_api_key_for_valid_user(session):
    """Проверяем что запрос api ключа возвращает статус 200
    и в результате содержится key"""

    assert session['status'] == 200
    assert session['key']