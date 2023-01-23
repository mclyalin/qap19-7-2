import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    """API библиотека к веб приложению Pet Friends"""

    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru'

    def get_api_key(self, email: str, password: str) -> tuple:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с уникальным ключем пользователя, найденного по указанным email и паролем"""

        endpoint = 'api/key'
        url = f'{self.base_url}/{endpoint}'
        headers = {
            'email': email,
            'password': password,
        }
        response = requests.get(url, headers=headers)
        status = response.status_code
        data = response.json() if status == 200 else {}
        key = data.get('key')
        return status, key

    def get_pets(self, auth_key: str, filter: str = '') -> tuple:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списком наденных питомцев, совпадающих с фильтром. На данный момент фильтр может иметь
        либо пустое значение - получить список всех питомцев, либо 'my_pets' - получить список
        собственных питомцев"""

        endpoint = 'api/pets'
        url = f'{self.base_url}/{endpoint}'
        headers = {'auth_key': auth_key}
        params = {'filter': filter}
        response = requests.get(url, headers=headers, params=params)
        status = response.status_code
        result = response.json() if status == 200 else {}
        return status, result

    def add_pet_simple(self, auth_key: str, name: str, animal_type: str, age: int) -> tuple:
        """Метод отправляет на сервер данные о добавляемом питомце без фотои возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""

        endpoint = 'api/create_pet_simple'
        url = f'{self.base_url}/{endpoint}'
        headers = {'auth_key': auth_key}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        response = requests.post(url, headers=headers, data=data)
        status = response.status_code
        result = ''
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text
        return status, result

    def add_pet(
        self, auth_key: str, name: str, animal_type: str, age: int, pet_photo: str) -> tuple:
        """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""

        endpoint = 'api/pets'
        url = f'{self.base_url}/{endpoint}'
        format = pet_photo.split('.')[-1]
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': str(age),
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), f'image/{format}'),
            }
        )
        headers = {
            'auth_key': auth_key,
            'Content-Type': data.content_type,
        }
        response = requests.post(url, headers=headers, data=data)
        status = response.status_code
        result = ''
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text
        return status, result

    def add_pet_photo(self, auth_key: str, pet_id: str, pet_photo: str) -> tuple:
        """Метод отправляет на сервер фото питомца по указанному ID и возвращает статус
        запроса на сервер и результат в формате JSON с данными обновленного питомца"""

        endpoint = 'api/pets/set_photo'
        url = f'{self.base_url}/{endpoint}/{pet_id}'
        format = pet_photo.split('.')[-1]
        data = MultipartEncoder(
            fields={'pet_photo': (pet_photo, open(pet_photo, 'rb'), f'image/{format}')}
        )
        headers = {
            'auth_key': auth_key,
            'Content-Type': data.content_type,
        }
        response = requests.post(url, headers=headers, data=data)
        status = response.status_code
        result = ''
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text
        return status, result

    def delete_pet(self, auth_key: str, pet_id: str) -> tuple:
        """Метод отправляет на сервер запрос на удаление питомца по указанному ID и возвращает
        статус запроса и результат в формате JSON с текстом уведомления о успешном удалении.
        На сегодняшний день тут есть баг - в result приходит пустая строка, но status при этом = 200"""

        endpoint = 'api/pets'
        url = f'{self.base_url}/{endpoint}/{pet_id}'
        headers = {'auth_key': auth_key}
        response = requests.delete(url, headers=headers)
        status = response.status_code
        result = ''
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text
        return status, result

    def update_pet(
        self, auth_key: str, pet_id: str, name: str, animal_type: str, age: int) -> tuple:
        """Метод отправляет запрос на сервер об обновлении данных питомца по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлённыи данными питомца"""

        endpoint = 'api/pets'
        url = f'{self.base_url}/{endpoint}/{pet_id}'
        headers = {'auth_key': auth_key}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        response = requests.put(url, headers=headers, data=data)
        status = response.status_code
        result = ''
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text
        return status, result
