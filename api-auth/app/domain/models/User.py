from sqlmodel import SQLModel, Field
from pydantic import EmailStr, validator
from ..security import crypt


class User(SQLModel, table=True):
    __tablename__ = 'users'

    id: int = Field(default=None, primary_key=True)
    email: EmailStr = Field(unique=True)
    password: str

    @validator('password')
    def password_min_len(cls, password) -> str:
        if len(password) < 8:
            raise ValueError('Password must have at least eight characters.')
        return password

class UserIn(User, table=False):
    confirm_password: str

    @validator('password')
    def passwords_must_match(cls, password, values) -> str:
        if 'confirm_password' in values and password != values.get('confirm_password'):
            raise ValueError('Passwords do not match.')
        return crypt.hash_password(password)