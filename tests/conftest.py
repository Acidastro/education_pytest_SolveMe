# Фикстуры служат для пре-реквизита. Это куски кода, которые будут выполняться до/во время/после теста.
# Фикстуры не нужно импортировать в основной файл тестов,
# т.к. программа их автоматически подтягивает из файла conftest.py,
# определяет фикстуры благодаря декоратору @pytest.fixture, достаточно в параметрах теста
# указать название функции текстуры. Так же тест будет принимать в параметры результат выполнения фикстуры
# scope='session' позволяет кешировать результат вычисления фикстуры и не вычислять его каждый раз
# autouse=True позволяет автоматически выполнять фикстуру для каждого теста (не рекомендуется).
# Главный conftest доступен всем файлам, но если conftest лежит в нижней директории,
# то будет доступен только тем файлам, которые в нем находятся (области видимости (глобальные/локальные)).
#

import pytest
from random import randrange
from src.generators.player import Player


@pytest.fixture
def get_number():
    """
    Вернет рандомное число от 1 до 1000 с шагом 5
    :return: int
    """
    return randrange(1, 1000, 5)


def _calculate(a: int, b: int):
    """
    Локальная функция для фикстуры, что бы принимать аргументы от тестов, и выполнять
    какие-либо действия с этими аргументами, затем возвращать обратно тесту.

    :param a: int
    :param b: int
    :return: int
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    return None


@pytest.fixture
def calculate():
    """
    Вызывает локальную функцию для сложения двух чисел.
    :return: Функция калькулятор
    """
    return _calculate


@pytest.fixture
def make_number():
    """
    make random number
    :return: int
    """
    print('Im getting number')
    number = randrange(0, 1000)
    yield number  # можно ничего не передавать в yield
    # Здесь делает паузу для выполнения теста,
    # затем снова возвращается к фикстуре
    print(f'Number at home {number}')


@pytest.fixture
def get_player_generator():
    return Player()
