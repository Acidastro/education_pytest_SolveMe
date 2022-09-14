"""
Содержит класс с перечислением возможных гендеров
"""
from enum import Enum


class Gender(Enum):
    female = 'female'
    male = 'male'


class Status(Enum):
    active = 'active'
    inactive = 'inactive'

class UserErrors(Enum):
    WRONG_EMAIL = 'Email doesnt contain @'