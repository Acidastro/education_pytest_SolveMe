"""
Основной файл, содержащий функции, которые запускаются при тестировании
Для одновременного запуска всех тестов проекта:
pytest -s -v tests


"""

import pytest
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

# @pytest.mark.skip
def test_getting_users_list(get_users):
    # print(response.__getstate__())  # Показывает внутреннюю информацию документа
    Response(get_users).assert_status_code(200).validate(User)


def test_getting_number(get_number):
    print(get_number)  # Печатает результат фикстуры


def test_getting_calculate(calculate):
    print('Калькулятор', calculate(2, 3))


@pytest.mark.production
@pytest.mark.development
def test_getting_users_id(make_number):
    print(make_number)
    pass


@pytest.mark.production
@pytest.mark.skip('[ISSUE-23414] Issue with network connection')
def test_skip():
    """
    Что бы не коментить тест, который в данный момент не пригодится,
    его можно скипать (не запускать) issue - проблема. Можно описать в комментарии
    проблему бага.

    """
    assert 1 == 1


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, 2, 1),
    (-1, -2, -3),
    ('b', -2, None),
    ('b', 'b', None)
])
def test_calculator(first_value, second_value, result, calculate):
    """
    Для того, что бы не писать много одинаковых тестов с разными переменными, существует parametrize. Он позволяет
    в одном тесте сделать сразу много проверок. В кортеже прописываются два значения на вход и ожидаемый результат.
    Функция автоматически подставляет их по очереди и запускает с ними тесты.
    """
    assert calculate(first_value, second_value) == result
