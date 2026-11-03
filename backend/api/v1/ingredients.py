from typing import Annotated

from database import SessionDep
from fastapi import APIRouter, Depends
from schemas.ingredient_schemas import IngredientCreate, IngredientRead
from services.ingredient_service import IngredientService

router = APIRouter(prefix="/ingredients", tags=["ingredients"])


def get_ingredient_service(session: SessionDep) -> IngredientService:
    return IngredientService(session)


IngredientServiceDep = Annotated[IngredientService, Depends(get_ingredient_service)]


@router.get("", response_model=list[IngredientRead])
def get_ingredients(service: IngredientServiceDep):
    return service.list_ingredients()


@router.post("", response_model=IngredientRead, status_code=201)
def post_ingredient(service: IngredientServiceDep, ingredient: IngredientCreate):
    return service.add_ingredient(ingredient)
