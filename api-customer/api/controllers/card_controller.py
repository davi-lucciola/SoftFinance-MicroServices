from http import HTTPStatus
from fastapi import APIRouter, Response
from ..domain.models import Card
from ..domain.services import card_service


router = APIRouter(prefix='/cards', tags=['Customer Cards'])


@router.get('/')
async def find_all_cards() -> Response: 
    return Response(card_service.find_all(), HTTPStatus.OK)

@router.get('/{id}')
async def detail_card(id: int) -> Response:
    return Response(card_service.find_by_id(id), HTTPStatus.OK)

@router.post('/')
async def register_card(card: Card) -> Response:
    return Response({
        'detail': 'Card successfully registered'
    }, HTTPStatus.OK)

@router.delete('/{id}')
async def delete_card():
    pass
