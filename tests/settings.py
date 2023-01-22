token = 'eyJlbWFpbCI6ICJ4YWxheDQ4MTIxQHhlZ2dlLmNvbSIsICJwYXNzd29yZCI6ICJLaXZBa25aY3M1eWVwIn0='
filter = 'my_pets'
images = [
    'images/pet1.png',
    'images/pet2.jpg',
    'images/pet3.pdf',
    ]

data = {
    '255 symbols': 'x' * 255,
    'more than 1000 symbols': 'x' * 1001,
    'russian': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
    'RUSSIAN': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper(),
    'chinese': '的一是不了人我在有他这为之大来以个中上们',
    'specials': '|\\/!@#$%^&*()-_=+`~?"№;:[]{}',
    'digit': 123,
    }

test_data = {
    'email': 'xalax48121@xegge.com',
    'password': 'KivAknZcs5yep',
    'token': 'eyJlbWFpbCI6ICJ4YWxheDQ4MTIxQHhlZ2dlLmNvbSIsICJwYXNzd29yZCI6ICJLaXZBa25aY3M1eWVwIn0=',
    'filter': 'my_pets',
    'pets': [
      {
        'name': 'Барбоскин',
        'animal_type': 'двортерьер',
        'age': 4,
      },
      {
        'name': 'Суперкот',
        'animal_type': 'кот',
        'age': 3,
      },
      {
        'name': 'Мурзик',
        'animal_type': 'Котэ',
        'age': 5,
      },
    ],
    'images': [
      'images/pet1.png',
      'images/pet2.jpg',
      'images/pet3.pdf'
    ],
}

