# Фикстуры служат для пре-реквизита. Это куски кода, которые будут выполняться до/во время/после теста.
# Фикстуры не нужно импортировать в основной файл тестов,
# т.к. программа их автоматически подтягивает из файла conftest.py,
# определяет фикстуры благодаря декоратору @pytest.fixture, достаточно в параметрах теста
# указать название функции текстуры. Так же тест будет принимать в параметры результат выполнения фикстуры
# scope='session' позволяет кешировать результат вычисления фикстуры и не вычислять его каждый раз
# autouse=True позволяет автоматически выполнять фикстуру для каждого теста (не рекомендуется)
import pytest
import requests

from configuration import SERVICE_URL



@pytest.fixture(scope='session', autouse=False)
def say_hello():
    print('Hello')
    return 14


@pytest.fixture
def get_users():
    response = requests.get(SERVICE_URL)
    return response