from fastapi import HTTPException, status
from models.recipes import Recipe
from schemas.recipe_schemas import RecipeCreate, RecipeUpdate
from sqlalchemy.orm import Session


class RecipeService:
    def __init__(self, session: Session) -> None:
        self._db = session

    def list_recipes(self) -> list[Recipe]:
        return self._db.query(Recipe).all()

    def add_recipe(self, recipe: RecipeCreate):
        db_recipe = Recipe(**recipe.model_dump())
        self._db.add(db_recipe)
        self._db.commit()
        self._db.refresh(db_recipe)
        return db_recipe

    def delete_recipe(self, recipe_id: int):
        recipe = self._db.query(Recipe).filter(Recipe.recipe_id == recipe_id).first()

        if recipe is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found"
            )

        self._db.delete(recipe)
        self._db.commit()
        return recipe

    def update_recipe(self, recipe: RecipeUpdate, recipe_id: int):
        db_recipe = self._db.query(Recipe).filter(
            Recipe.recipe_id == recipe_id
        ).first()

        if db_recipe is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found"
            )

        for field, value in recipe.model_dump(exclude_unset=True).items():
            setattr(db_recipe, field, value)

        self._db.commit()
        self._db.refresh(db_recipe)
        return db_recipe
