"""
builder (строитель) для словаря
Некий класс, который по умолчанию создает и меняет значения, создает массив данных.
"""

from src.enums.user_enums import Status
from src.generators.player_localization import PlayerLocalization


class Player:

    def __init__(self):
        self.result = dict()
        self.reset()  # автонаполнение массива

    def set_status(self, status=Status.active.value):
        """
        Задать статус
        :param status:
        :return:
        """
        self.result['account_status'] = status
        return self

    def set_balance(self, balance=0):
        """
        Задать баланс
        :param balance:
        :return:
        """
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar='google.com'):
        """
        Задать аватар
        :param avatar:
        :return:
        """
        self.result['avatar'] = avatar
        return self

    def reset(self):
        """
        Заполнить по умолчанию.
        :return:
        """
        self.set_status()
        self.set_avatar()
        self.set_balance()
        self.result['localize'] = {
            'en': PlayerLocalization('en_US').build(),
            'ru': PlayerLocalization('ru_RU').build()
        }

        return self

    def update_inner_generator(self, key, generator):
        """
        Меняет параметр
        :param key: прописываем любой нужный нам ключ
        :param generator: PlayerLocalization
        :return:
        """
        self.result[key] = generator.build()
        return self

    def build(self):
        """
        Закончить заполнение.
        :return:
        """
        return self.result
