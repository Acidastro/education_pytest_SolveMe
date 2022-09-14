"""
Файл содержит различные ответы к ошибкам
"""
from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Received status code isnt equal expected.'
    WRONG_ELEMENT_COUNT = 'Number of items isnt equal to expected'
