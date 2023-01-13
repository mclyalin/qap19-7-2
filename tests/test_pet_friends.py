import os
from qap19_7_2.api import PetFriends
from tests.settings import test_data

pf = PetFriends()
valid_email, valid_password, filter, test_pets, images = test_data.values()


def test_get_api_key_for_valid_user():
    """Проверяем что запрос api ключа возвращает статус 200
    и в результате содержится key"""

    status, result = pf.get_api_key(valid_email, valid_password)

    assert status == 200
    assert 'key' in result
    assert result['key'] != ''


def test_get_all_pets_with_valid_key():
    """Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этот ключ
    запрашиваем список всех питомцев и проверяем что список не пустой"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key)

    assert status == 200
    assert 'pets' in result
    assert len(result['pets']) > 0


def test_add_pet_with_valid_data():
    """Проверяем что можно добавить питомца с корректными данными"""

    name, animal_type, age = test_pets[0].values()
    pet_photo = os.path.join(os.path.dirname(__file__), images[0])
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert 'name' in result
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter)

    # Проверяем - если список своих питомцев пустой, то добавляем питомца
    # и снова запрашиваем список питомцев пользователя
    if len(my_pets['pets']) == 0:
        name, animal_type, age = test_pets[0].values()
        pf.add_new_pet_simple(auth_key, name, animal_type, age)
        _, my_pets = pf.get_list_of_pets(auth_key, filter)

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert pet_id not in str(my_pets)


def test_successful_update_self_pet_info():
    """Проверяем возможность обновления информации о питомце"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter)

    # Проверяем - если список своих питомцев пустой, то добавляем питомца
    # и снова запрашиваем список питомцев пользователя
    if len(my_pets['pets']) == 0:
        name, animal_type, age = test_pets[0].values()
        pf.add_new_pet_simple(auth_key, name, animal_type, age)
        _, my_pets = pf.get_list_of_pets(auth_key, filter)

    my_pet_id = my_pets['pets'][0]['id']
    name, animal_type, age = test_pets[1].values()
    status, result = pf.update_pet_info(auth_key, my_pet_id, name, animal_type, age)

    assert status == 200
    assert 'name' in result
    assert result['name'] == name


def test_add_pet_simple_with_valid_data():
    """Проверяем что можно добавить питомца без фото с корректными данными"""

    name, animal_type, age = test_pets[-1].values()
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    assert status == 200
    assert 'name' in result
    assert result['name'] == name


def test_get_user_pets_with_valid_key():
    """Проверяем что запрос питомцев пользователя возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этот ключ
    запрашиваем список всех питомцев и проверяем что список не пустой"""

    name, animal_type, age = test_pets[0].values()
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pet = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert 'pets' in result
    assert len(result['pets']) > 0
    assert result['pets'][0]['id'] == my_pet['id']


def test_add_pet_png_photo_():
    """Проверяем что можно добавить питомцу фото в формате PNG"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter)

    # Проверяем - если список своих питомцев пустой, то добавляем питомца
    # и снова запрашиваем список питомцев пользователя
    if len(my_pets['pets']) == 0:
        name, animal_type, age = test_pets[0].values()
        pf.add_new_pet_simple(auth_key, name, animal_type, age)
        _, my_pets = pf.get_list_of_pets(auth_key, filter)

    my_pet_id = my_pets['pets'][0]['id']
    png = os.path.join(os.path.dirname(__file__), images[0])
    status, result = pf.add_pet_photo(auth_key, my_pet_id, png)

    assert status == 200
    assert 'pet_photo' in result
    assert result['pet_photo'] != ''


def test_add_pet_jpg_photo_():
    """Проверяем что можно добавить питомцу фото в формате JPG"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter)

    # Проверяем - если список своих питомцев пустой, то добавляем питомца
    # и снова запрашиваем список питомцев пользователя
    if len(my_pets['pets']) == 0:
        name, animal_type, age = test_pets[0].values()
        pf.add_new_pet_simple(auth_key, name, animal_type, age)
        _, my_pets = pf.get_list_of_pets(auth_key, filter)

    my_pet_id = my_pets['pets'][0]['id']
    jpg = os.path.join(os.path.dirname(__file__), images[1])
    status, result = pf.add_pet_photo(auth_key, my_pet_id, jpg)

    assert status == 200
    assert 'pet_photo' in result
    assert result['pet_photo'] != ''


def test_failed_get_api_key_for_invalid_email():
    """Проверяем что, в соответствии с документацией, запрос api ключа
    c невалидным email возвращает статус 403 и результат не содержит key"""

    invalid_email = test_data.get('invalid_email', 'a@b.cd')
    status, result = pf.get_api_key(invalid_email, valid_password)

    assert status == 403
    assert 'key' not in result


def test_failed_get_api_key_for_valid_email_with_invalid_password():
    """Проверяем что, в соответствии с документацией, запрос api ключа
    c невалидным паролем возвращает статус 403 и результат не содержит key"""

    invalid_password = valid_password[::-1]
    status, result = pf.get_api_key(valid_email, invalid_password)

    assert status == 403
    assert 'key' not in result


def test_failed_get_all_pets_with_invalid_key():
    """Проверяем что, в соответствии с документацией, запрос всех питомцев
    c невалидным ключом возвращает статус 403 и результат не содержит питомцев"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key['key'] = auth_key['key'][::-1]
    status, result = pf.get_list_of_pets(auth_key)

    assert status == 403
    assert 'pets' not in result


def test_failed_add_pet_simple_with_invalid_data():
    """Проверяем что, в соответствии с документацией, запрос на добавление питомца
    с некорректными данными возвращает статус 400 и результат не содержит питомца"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, '', '', '')

    assert status == 400
    assert 'name' not in result


def test_failed_add_pet_simple_with_script_in_name():
    """Проверяем что запрос на добавление питомца с именем, содержащим код,
    возвращает статус 400 и результат не содержит питомца"""

    danger_name = '<script>alert("boom!")</script>'
    _, animal_type, age = test_pets[0].values()
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, danger_name, animal_type, age)

    assert status == 400
    assert 'name' not in result


def test_failed_add_pet_pdf_photo_():
    """Проверяем что, в соответствии с документацией, запрос на добавление фото питомца
    в неподдерживаемом формате (PDF) возвращает статус 400 и результат не содержит питомца"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter)

    # Проверяем - если список своих питомцев пустой, то добавляем питомца
    # и снова запрашиваем список питомцев пользователя
    if len(my_pets['pets']) == 0:
        name, animal_type, age = test_pets[0].values()
        pf.add_new_pet_simple(auth_key, name, animal_type, age)
        _, my_pets = pf.get_list_of_pets(auth_key, filter)

    my_pet_id = my_pets['pets'][0]['id']
    pdf = os.path.join(os.path.dirname(__file__), images[-1])
    status, result = pf.add_pet_photo(auth_key, my_pet_id, pdf)

    assert status == 400
    assert 'pet_photo' not in result
