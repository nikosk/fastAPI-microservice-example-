import re

from pydantic import BaseModel, validator, Field

email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class UserForm(BaseModel):
    email: str = Field(None, regex=email_pattern)
    password: str = Field(None, min_length=6)
    passwordConfirm: str

    @validator('email')
    def must_be_valid_email(cls, v):
        if not re.fullmatch(email_pattern, v):
            raise ValueError('Invalid email')
        return v

    @validator('passwordConfirm')
    def passwords_must_match(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v
