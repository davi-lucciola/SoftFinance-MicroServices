from http import HTTPStatus
from fastapi import APIRouter, Response



router = APIRouter(prefix='/cards', tags=['Custumer Cards'])


@router.get('/')
async def find_all_cards() -> Response:
    return Response(
        
    , HTTPStatus.OK)