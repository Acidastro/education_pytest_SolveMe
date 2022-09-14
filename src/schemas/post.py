"""
Файл содержит схемы для валидирования с помощью jsonschema
"""

# {'id': 1, 'title': 'Post 1'}
POST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'number'},  # свойства которые обязательно должны быть у id
        'title': {'type': 'string'},

    },
    'required': ['id']  # обязательно должен быть id
}
