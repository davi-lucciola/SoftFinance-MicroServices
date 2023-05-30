from ormar import ModelMeta
from ...infrastructure.database import database, metadata


class BaseMeta(ModelMeta):
    database = database
    metadata = metadata