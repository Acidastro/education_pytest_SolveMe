"""
Файл содержит схемы для валидирования с помощью pydantic
"""
# {'id': 1, 'title': 'Post 1'}

from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int = Field(le=2)  # Больше или равно 2. Field содержит много встроенных валидаций
    # id: int
    title: str
    # name: str = Field('_name')

    # @validator('id')
    # def check_that_id_is_less_than_two(cls, v):  # Кастомный валидатор, который проверяет, id < 2
    #     if v > 2:
    #         raise ValueError('Id isnt less than two')
    #     else:
    #         return v
