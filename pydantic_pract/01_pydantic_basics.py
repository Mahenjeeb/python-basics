from pydantic import BaseModel, Field, field_validator, model_validator
import re

class User(BaseModel):
    user_name: str = Field(
        ...,
        min_length=3,
        max_length=20
    ),
    password: str = Field(
        ...,
        min_length=8
    ),
    confirm_password: str = Field(
        ...,
        min_length=8
    ),
    email: str = Field(
        pattern=r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
        )
user = {
    "user_name": "Mahenjeeb",
    "password": "12345678",
    "confirm_password": "12345678",
    "email": "mahenjeeb345gmail.com"
}

userModel = User(**user)
print(userModel)