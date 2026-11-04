from typing import Annotated

from database import SessionDep
from fastapi import APIRouter, Depends
from schemas.recipe_schemas import RecipeCreate, RecipeUpdate, RecipeRead
from services.recipe_service import RecipeService

router = APIRouter(prefix="/recipes", tags=["recipes"])


def get_recipe_service(session: SessionDep) -> RecipeService:
    return RecipeService(session)


RecipeServiceDep = Annotated[RecipeService, Depends(get_recipe_service)]


@router.get("", response_model=list[RecipeRead])
def get_recipes(service: RecipeServiceDep):
    return service.list_recipes()


@router.post("", response_model=RecipeRead, status_code=201)
def post_recipe(service: RecipeServiceDep, recipe: RecipeCreate):
    return service.add_recipe(recipe)


@router.delete("/{recipe_id}", response_model=RecipeRead)
def delete_recipe(service: RecipeServiceDep, recipe_id: int):
    return service.delete_recipe(recipe_id)


@router.patch("/{recipe_id}", response_model=RecipeRead)
def update_recipe(service: RecipeServiceDep, recipe_id: int, recipe: RecipeUpdate):
    return service.update_recipe(recipe, recipe_id)
