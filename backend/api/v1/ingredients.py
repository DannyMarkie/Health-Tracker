from typing import Annotated

from database import Connection
from fastapi import APIRouter, Depends
from models.ingredients import IngredientsModel
from services.ingredient_service import IngredientService

router = APIRouter()


def get_ingredient_service() -> IngredientService:
    return IngredientService(session=Connection())


IngredientServiceDep = Annotated[IngredientService, Depends(get_ingredient_service)]


@router.get("/ingredients")
async def get_ingredients(service: IngredientServiceDep):
    return service.list_ingredients()


@router.post("/ingredients", response_model=None)
async def post_ingredient(service: IngredientServiceDep, ingredient: IngredientsModel):
    return service.add_ingredient(ingredient)
