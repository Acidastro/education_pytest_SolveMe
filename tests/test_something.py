"""
Основной файл, содержащий функции, которые запускаются при тестировании
"""

import requests
from jsonschema import validate
from configuration import SERVICE_URL
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


def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    # print(response.__getstate__())  # Показывает внутреннюю информацию документа
    test_object.assert_status_code(300).validate(User)

