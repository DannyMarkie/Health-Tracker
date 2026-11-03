from typing import Annotated

from database import SessionDep
from fastapi import APIRouter, Depends
from schemas.unit_schemas import UnitRead
from services.unit_service import UnitService

router = APIRouter(prefix="/units", tags=["units"])


def get_unit_service(session: SessionDep) -> UnitService:
    return UnitService(session)


UnitServiceDep = Annotated[UnitService, Depends(get_unit_service)]


@router.get("", response_model=list[UnitRead])
def get_units(service: UnitServiceDep):
    return service.list_units()
