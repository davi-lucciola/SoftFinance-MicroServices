from ..security import crypt
from pydantic import EmailStr
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    __tablename__ = 'users'

    id: int = Field(default=None, primary_key=True)
    email: EmailStr = Field(unique=True)
    password: str

    def hash_password(self) -> None:
        self.password: str = crypt.hash_password(self.password)

class UserIn(SQLModel):
    email: EmailStr
    password: str
    confirm_password: str

    def passwords_match(self) -> bool:
        return self.password == self.confirm_password

class UserLogin(SQLModel):
    email: EmailStr
    password: str

    def passwords_match(self, hashed_password: str) -> bool:
        return crypt.verify_password(self.password, hashed_password)