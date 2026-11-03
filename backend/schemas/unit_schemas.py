from pydantic import BaseModel, ConfigDict, Field


class UnitBase(BaseModel):
    unit_code: str = Field(min_length=1, max_length=255)
    unit_display_name: str = Field(min_length=1, max_length=255)


class UnitRead(UnitBase):
    model_config = ConfigDict(from_attributes=True)
    unit_id: int
