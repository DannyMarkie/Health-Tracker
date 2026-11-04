from typing import Annotated

from database import SessionDep
from fastapi import APIRouter, Depends
from schemas.recipeingredient_schemas import (
    RecipeIngredientCreate,
    RecipeIngredientRead,
    RecipeIngredientUpdate,
)
from services.recipeingredient_service import RecipeIngredientService

router = APIRouter(prefix="/recipeingredients", tags=["recipe_ingredients"])


def get_recipeingredient_service(session: SessionDep) -> RecipeIngredientService:
    return RecipeIngredientService(session)


RecipeIngredientServiceDep = Annotated[
    RecipeIngredientService, Depends(get_recipeingredient_service)
]


@router.get("", response_model=list[RecipeIngredientRead])
def get_recipeingredients(service: RecipeIngredientServiceDep):
    return service.list_recipe_ingredients()


@router.post("", response_model=list[RecipeIngredientRead], status_code=201)
def post_bulk_recipeingredients(
    service: RecipeIngredientServiceDep,
    recipe_ingredients: list[RecipeIngredientCreate],
):
    return service.bulk_add_ingredients(recipe_ingredients)


@router.patch("", response_model=RecipeIngredientRead)
def update_recipeingredient(
    service: RecipeIngredientServiceDep, recipe_ingredient: RecipeIngredientUpdate
):
    return service.update_recipe_ingredient(recipe_ingredient)


@router.delete("/{recipe_id}/{ingredient_id}", response_model=RecipeIngredientRead)
def remove_recipeingredient(
    service: RecipeIngredientServiceDep, recipe_id: int, ingredient_id: int
):
    return service.remove_recipe_ingredients(recipe_id, ingredient_id)
