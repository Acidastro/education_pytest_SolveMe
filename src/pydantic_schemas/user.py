from pydantic import BaseModel, validator
from src.enums.user_enums import Gender, Status, UserErrors


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Gender  # Наши кастомные гендеры
    status: Status

    @validator('email')
    def check_that_dog_presented_in_email_address(cls, email):
        if '@' in email:
            return email
        raise ValueError(UserErrors.WRONG_EMAIL.value)
