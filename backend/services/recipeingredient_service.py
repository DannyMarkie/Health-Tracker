from fastapi import HTTPException, status
from models.recipe_ingredients import RecipeIngredient
from schemas.recipeingredient_schemas import (
    RecipeIngredientCreate,
    RecipeIngredientUpdate,
)
from sqlalchemy.orm import Session


class RecipeIngredientService:
    def __init__(self, session: Session) -> None:
        self._db = session

    def list_recipe_ingredients(self) -> list[RecipeIngredient]:
        return self._db.query(RecipeIngredient).all()

    def bulk_add_ingredients(self, recipe_ingredients: list[RecipeIngredientCreate]):
        db_recipe_ingredients = [
            RecipeIngredient(**recipe_ingredient.model_dump())
            for recipe_ingredient in recipe_ingredients
        ]

        self._db.add_all(db_recipe_ingredients)
        self._db.commit()

        for recipe_ingredient in db_recipe_ingredients:
            self._db.refresh(recipe_ingredient)
        return db_recipe_ingredients

    def update_recipe_ingredient(self, recipe_ingredient: RecipeIngredientUpdate):
        db_recipe_ingredient = (
            self._db.query(RecipeIngredient)
            .filter(
                RecipeIngredient.recipe_id == recipe_ingredient.recipe_id,
                RecipeIngredient.ingredient_id == recipe_ingredient.ingredient_id,
            )
            .first()
        )

        if db_recipe_ingredient is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Recipe Ingredient not found",
            )

        for field, value in recipe_ingredient.model_dump(exclude_none=True).items():
            setattr(db_recipe_ingredient, field, value)

        self._db.commit()
        self._db.refresh(db_recipe_ingredient)
        return db_recipe_ingredient

    def remove_recipe_ingredient(self, recipe_id: int, ingredient_id: int):
        recipe_ingredient = (
            self._db.query(RecipeIngredient)
            .filter(
                RecipeIngredient.recipe_id == recipe_id,
                RecipeIngredient.ingredient_id == ingredient_id,
            )
            .first()
        )

        if recipe_ingredient is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Recipe Ingredient not found",
            )

        self._db.delete(recipe_ingredient)
        self._db.commit()
        return recipe_ingredient
