###### Учебный проект QAP ([Skillfactory](https://skillfactory.ru)
### Тестирование [REST API](https://petfriends.skillfactory.ru/apidocs/#/) сайта [Petfriends](https://petfriends.skillfactory.ru).  

Что сделано:
- реализована библиотека API-методов в соответствии с документацией (Swagger);
- описаны позитивные и негативные пользовательские сценарии и составлены тест-кейсы;
- реализованы автотесты;

В проекте применялись следующие инструменты:
- сервис временной почты [tempmail+](https://tempmail.plus) для авторизации;
- сервис [Random string generator](http://www.unit-conversion.info/texttools/random-string-generator/) для генерации тестовых данных;
- техники граничных значений и классы эквивалентности для оптимизации тестовых данных;
- Chrome DevTools для анализа ответов сервера;

Тест-кейсы и сценарии доступны [здесь](https://docs.google.com/spreadsheets/d/1R-QJppMTwIR1tBF9a4v1Fets-pBpRIr9svnTjgOEfCY/edit?usp=sharing).
***
**Структура проекта:**
+ qap19-7-2/api.py - библиотека методов
+ tests/ - файлы тестов
+ settings.py - данные для тестирования

**Для запуска тестов:**
1. склонировать репозиторий
1. установить [poetry](https://python-poetry.org/)
2. в директории проекта выполнить комманду `poetry install`
3. запуск тестов `poetry run pytest -v`
