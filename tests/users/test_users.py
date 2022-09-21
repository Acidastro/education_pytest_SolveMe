"""
Основной файл, содержащий функции, которые запускаются при тестировании
Для одновременного запуска всех тестов проекта:
pytest -s -v tests


"""

import requests
from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages
# from src.schemas.post import POST_SCHEMA
from src.baseclasses.response import Response
from src.pydantic_schemas.post import Post
from src.pydantic_schemas.user import User


# def test_getting_posts():
#     r = requests.get(url=SERVICE_URL)
#     response = Response(r)
#     response.assert_status_code(200).validate(Post)  # validate проверяется с помощью схемы Post написанной в pydantic
#
# # [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]


def test_getting_users_list(get_users):
    # print(response.__getstate__())  # Показывает внутреннюю информацию документа
    Response(get_users).assert_status_code(200).validate(User)


def test_getting_number(get_number):
    print(get_number)  # Печатает результат фикстуры


def test_getting_calculate(calculate):
    print('Калькулятор', calculate(2, 3))


def test_getting_users_id(make_number):
    print(make_number)
    pass
