from pydantic import BaseModel, ConfigDict, Field


class RecipeBase(BaseModel):
    recipe_name: str = Field(min_length=1, max_length=255)
    servings: int = Field(gt=0)


class RecipeCreate(RecipeBase):
    pass


class RecipeRead(RecipeBase):
    model_config = ConfigDict(from_attributes=True)
    recipe_id: int


class RecipeUpdate(BaseModel):
    recipe_name: str | None = Field(default=None, min_length=1, max_length=255)
    servings: int | None = Field(default=None, gt=0)
