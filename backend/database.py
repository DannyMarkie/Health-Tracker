from config import get_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(get_url())
Connection = sessionmaker(bind=engine)
