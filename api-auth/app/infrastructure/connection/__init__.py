from decouple import config
from sqlmodel import SQLModel
from sqlalchemy.engine import Engine, create_engine
from infrastructure.connection import *


DATABASE_URL: str = config('DATABASE_URL')
engine: Engine = create_engine(DATABASE_URL, pool_pre_ping=True)


def create_tables() -> None:
    SQLModel.metadata.create_all(engine)