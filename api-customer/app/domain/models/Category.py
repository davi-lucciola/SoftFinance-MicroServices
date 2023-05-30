from . import BaseMeta
from ormar import (
    Model, Integer, String, ForeignKeyField, ForeignKey
)


class Category(Model):
    class Meta(BaseMeta):
        tablename = 'categories'
    
    id: int = Integer(primary_key=True, autoincrement=True)
    name: str = String(min_length=1, max_length=255)
    color: str = String(min_length=10, max_length=255)
    icon: str = String(min_length=1, max_length=255)
    # user_id: int = ForeignKeyField(foreing_key=ForeignKey('users.id'))