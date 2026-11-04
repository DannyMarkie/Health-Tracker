from typing import Annotated

from database import SessionDep
from fastapi import APIRouter, Depends
from schemas.ingredient_schemas import (
    IngredientCreate,
    IngredientRead,
    IngredientUpdate,
)
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


@router.patch("/{ingredient_id}", response_model=IngredientRead)
def update_ingredient(
    service: IngredientServiceDep, ingredient_id: int, ingredient: IngredientUpdate
):
    return service.update_ingredient(ingredient_id, ingredient)


@router.delete("/{ingredient_id}", response_model=IngredientRead)
def remove_ingredient(service: IngredientServiceDep, ingredient_id: int):
    return service.remove_ingredient(ingredient_id)
