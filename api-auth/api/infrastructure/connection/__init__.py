from decouple import config
from sqlmodel import SQLModel
from sqlalchemy.engine import Engine, create_engine


def get_connection_string() -> str:
    HOST = config('HOST')
    PORT = config('PORT')
    USER = config('POSTGRES_USER')
    PASSWORD = config('POSTGRES_PASSWORD')
    DB = config('POSTGRES_DB')

    return f'postgresql+psycopg2://' + \
    f'{USER}{f":{PASSWORD}" if PASSWORD != "" else ""}@{HOST}:{PORT}/{DB}'


print(get_connection_string())
DATABASE_URL: str = get_connection_string()
engine: Engine = create_engine(DATABASE_URL, pool_pre_ping=True)


def create_tables() -> None:
    SQLModel.metadata.create_all(engine)