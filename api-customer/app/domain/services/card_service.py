from http import HTTPStatus
from fastapi import HTTPException
from ..models import Card


class CardService:
    async def find_all(self) -> list[Card]:
        cards: list[Card] = await Card.objects.all()
        if len(cards) == 0:
            raise HTTPException (
                status_code = HTTPStatus.NO_CONTENT
            )
        
        return cards

    async def find_by_id(self, id: int) -> Card:
        card: Card | None = await Card.objects.get_or_none(Card.id == id)
        if card is None:
            raise HTTPException(
                status_code = HTTPStatus.NOT_FOUND,
                detail = 'Card not found'
            )

        return card

    async def register_card(self, card: Card):
        await card.save()

    async def delete_card(self, card_id: int):
        card: Card = await self.find_by_id(card_id)
        await card.delete()