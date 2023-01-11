import requests


BASE_URL = 'https://petfriends.skillfactory.ru'
user = {
  'email': 'xalax48121@xegge.com',
  'password': 'KivAknZcs5yep'
}

def get_auth_key(email: str, password: str):
  endpoint = 'api/key'
  url = f'{BASE_URL}/{endpoint}'
  headers = {'email': email, 'password': password}
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    return response.json().get('key')

auth_key = get_auth_key(user.get('email'), user.get('password'))

def add_pet_simple(name: str, animal_type: str, age: int):
  endpoint = 'api/create_pet_simple'
  url = f'{BASE_URL}/{endpoint}'
  headers = {'auth_key': auth_key}
  data = {'name': name, 'animal_type': animal_type, 'age': age}
  response = requests.post(url, headers=headers, data=data)
  if response.status_code == 200:
   return response.json()

def get_pets(filter=''):
  endpoint = 'api/pets'
  url = f'{BASE_URL}/{endpoint}'
  headers = {'auth_key': auth_key}
  params = {'filter': filter}
  response = requests.get(url, headers=headers, params=params)
  if response.status_code == 200:
    return response.json()

def remove_pet(id):
  endpoint = 'api/pets'
  url = f'{BASE_URL}/{endpoint}/{id}'
  headers = {'auth_key': auth_key}
  response = requests.delete(url, headers=headers)
  return response.status_code

def update_pet(id, **new_data):
  items = get_pets('my_pets').get('pets')
  filtered = filter(lambda item: item.get('id') == id, items)
  current = list(filtered)[0]
  data = {
    'name': current.get('name'),
    'animal_type': current.get('animal_type'),
    'age': int(current.get('age'))
  }

  endpoint = 'api/pets'
  url = f'{BASE_URL}/{endpoint}/{id}'
  headers = {'auth_key': auth_key}
  response = requests.put(url, headers=headers, data={**data, **new_data})
  return response.json()
