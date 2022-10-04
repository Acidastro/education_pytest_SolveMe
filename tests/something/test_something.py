import pytest
import requests
from src.generators.player_localization import PlayerLocalization

def test_something(get_number):
    assert 1 == 1
    print(get_number)


@pytest.mark.parametrize('status', [
    'ACTIVE',
    'BANNED',
    'DELETED',
    'INACTIVE'
])
def test_player_status(status, get_player_generator):
    """
    Тест с помощью автоматической генерации словаря.
    Тест с подменой статусов.
    :param status: прописано в mark.parametrize.
    :param get_player_generator: результат вызова фикстуры, которая генерирует ЭК Player
    :return:
    """
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize('balance', [
    '10',
    '0',
    '-10',
    'asd'
])
def test_player_balance(balance, get_player_generator):
    """
    Тест с помощью автоматической генерации словаря.
    Тест с подменой балансов.
    :param balance: прописано в mark.parametrize.
    :param get_player_generator: результат вызова фикстуры, которая генерирует ЭК Player
    :return:
    """
    print(get_player_generator.set_balance(balance).build())


@pytest.mark.parametrize('delete_key', [
    'account_status',
    'balance',
    'localize',
    'avatar'
])
def test_player_balance(delete_key, get_player_generator):
    """
    Тест с помощью автоматической генерации словаря.
    Тест по очереди удаляет один из ключей словаря.
    :param delete_key: ключ, который удалится, прописано в mark.parametrize.
    :param get_player_generator: результат вызова фикстуры, которая генерирует ЭК Player
    :return:
    """
    object_to_send = get_player_generator.build()  # создать словарь
    del object_to_send[delete_key]  # удалить из словаря ключ
    print(object_to_send)  # напечатать объект


def test_player_update_inner_generator(get_player_generator):
    """
    Тест с помощью автоматической генерации словаря.
    Тест меняет параметр localize
    :param get_player_generator: результат вызова фикстуры, которая генерирует ЭК Player
    :return:
    """
    object_to_send = get_player_generator.update_inner_generator(
        'localize', PlayerLocalization('fr_FR').set_number()
    ).build()
    print(object_to_send)
