from collections.abc import Iterator
from typing import Annotated

from config import get_url
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine(get_url())
SessionLocal = sessionmaker(bind=engine)


def get_session() -> Iterator[Session]:
    with SessionLocal() as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
