from sqlmodel import SQLModel, Relationship, Field
from datetime import datetime as dt
from . import  User


class Token(SQLModel, table=True):
    __tablename__ = 'tokens'

    id: int = Field(primary_key=True)
    initiated_at: dt
    expire_at: dt
    user_id: int = Field(nullable=False, foreign_key='users.id')
    acess_token: str

    user: User = Relationship()
