from decouple import config
from sqlmodel import SQLModel
from sqlalchemy.engine import Engine, create_engine


def get_connection_string() -> str:
    HOST = config('HOST')
    USER = config('POSTGRES_USER')
    PASSWORD = config('POSTGRES_PASSWORD')
    DB = config('POSTGRES_DB')

    return f'postgresql+psycopg2://' + \
    f'{HOST}/{DB}?user={USER}&password={PASSWORD}'


DATABASE_URL: str = get_connection_string()
print(DATABASE_URL)
engine: Engine = create_engine(DATABASE_URL, pool_pre_ping=True)


def create_tables() -> None:
    global engine
    SQLModel.metadata.create_all(engine)