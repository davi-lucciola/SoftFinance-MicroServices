from ormar import (
    Model, Integer, String, Decimal, ForeignKeyField, ForeignKey
)
from ...infrastructure.connection import database, metadata


class Card(Model):
    class Meta:
        tablename = 'cards'
        database = database
        metadata = metadata
    
    id: int = Integer(primary_key=True, autoincrement=True)
    bank: str = String(min_length=2, max_length=255,nullable=False)
    card_number: str = String(min_length=14, max_length=20)
    limit: float = Decimal(nullable=False, precision=9, scale=3)
    limit_used: float = Decimal(nullable=False, precision=9, scale=3)
    # user_id: int = ForeignKeyField(foreing_key=ForeignKey('users.id'))