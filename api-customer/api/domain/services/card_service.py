from http import HTTPStatus
from fastapi import HTTPException
from ..models import Card


async def find_all() -> list[Card]:
    cards: list[Card] = Card.objects.all()

    if len(cards) == 0:
        raise HTTPException (
            status_code = HTTPStatus.NO_CONTENT
        )
    
    return cards

async def find_by_id(id: int) -> Card:

    card: Card = Card.objects.get_or_none(Card.id == id)

    if card is None:
        raise HTTPException(
            status_code = HTTPStatus.NOT_FOUND,
            detail = 'Card not found'
        )

    return 

async def register_card(card: Card):
    pass