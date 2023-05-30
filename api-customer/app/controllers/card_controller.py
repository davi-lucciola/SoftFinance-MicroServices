from http import HTTPStatus
from fastapi import APIRouter, Depends
from ..domain.models import Card
from ..domain.services import CardService


router = APIRouter(prefix='/cards', tags=['Customer Cards'])


@router.get('/', status_code = HTTPStatus.OK)
async def find_all_cards(service: CardService = Depends(CardService)) -> list[Card]: 
    return await service.find_all()

@router.post('/', status_code = HTTPStatus.OK)
async def register_card(card: Card, service: CardService = Depends(CardService)) -> dict:
    await service.register_card(card)
    return {'detail': 'Card successfully registered'}

@router.get('/{id}', status_code = HTTPStatus.OK)
async def detail_card(id: int, service: CardService = Depends(CardService)) -> Card:
    return await service.find_by_id(id)

@router.delete('/{id}')
async def delete_card(id: int, service: CardService = Depends(CardService)) -> dict:
    await service.delete_card(id)
    return {'detail': 'Card successfully deleted'}
