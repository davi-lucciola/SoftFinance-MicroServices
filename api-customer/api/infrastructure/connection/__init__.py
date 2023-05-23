import os
from decouple import config
from databases import Database
from sqlalchemy import MetaData
from sqlalchemy.engine import Engine, create_engine


def get_connection_string() -> str:
    db_path = os.path.join(os.getcwd(), 'api', 'infrastructure')

    # HOST = config('HOST')
    # USER = config('POSTGRES_USER')
    # PASSWORD = config('POSTGRES_PASSWORD')
    DB = os.path.join(db_path, config('POSTGRES_DB'))

    # return f'postgresql+psycopg2://' + \
    # f'{HOST}/{DB}?user={USER}&password={PASSWORD}'
    return f'sqlite:///{DB}'


DATABASE_URL: str = get_connection_string()

engine: Engine = create_engine(DATABASE_URL, pool_pre_ping=True)
database: Database = Database(DATABASE_URL)
metadata: MetaData = MetaData()

def create_tables() -> None:
    global engine, metadata
    metadata.create_all(engine)
