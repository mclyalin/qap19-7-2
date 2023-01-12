import os
from qap19_7_2.app import PetFriends
from tests.settings import test_data

pf = PetFriends()
valid_email, valid_password, filter, test_pets, photos = test_data.values()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result

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
    pet_photo = os.path.join(os.path.dirname(__file__), photos[0])
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name

def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter)

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        name, animal_type, age = test_pets[0].values()
        pet_photo = os.path.join(os.path.dirname(__file__), photos[0])
        pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
        _, my_pets = pf.get_list_of_pets(auth_key, filter)

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, filter)

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()

def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(
            auth_key, my_pets['pets'][0]['id'], name, animal_type, age
        )

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception('There is no my pets')

def test_add_pet_simple_with_valid_data():
    """Проверяем что можно добавить питомца без фото с корректными данными"""

    name, animal_type, age = test_pets[-1].values()
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name

def test_get_user_pets_with_valid_key():
    """Проверяем что, после создания питомца, запрос питомцев пользователя возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этот ключ
    создаем нового питомца. Далее запрашиваем список питомцев пользователя и проверяем что в списке есть
    новый питомец"""

    pass

