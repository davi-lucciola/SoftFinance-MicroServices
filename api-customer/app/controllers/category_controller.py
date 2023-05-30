from http import HTTPStatus
from fastapi import APIRouter, Depends
from ..domain.models import Category
from ..domain.services import CategoryService


router = APIRouter(prefix='/categories', tags=['categories'])


@router.get('/', status_code = HTTPStatus.OK) 
async def find_all_categories(service: CategoryService = Depends(CategoryService)) -> list[Category]:
    pass

@router.post('/', status_code = HTTPStatus.OK) 
async def register_category(service: CategoryService = Depends(CategoryService)) -> dict:
    pass

@router.get('/{id}', status_code = HTTPStatus.OK) 
async def detail_category(id: int, service: CategoryService = Depends(CategoryService)) -> Category:
    pass

@router.delete('/{id}')
async def delete_category(id: int, service: CategoryService = Depends(CategoryService)) -> dict:
    pass
