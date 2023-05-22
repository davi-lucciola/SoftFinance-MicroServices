from . import engine
from sqlmodel import SQLModel
from sqlalchemy.orm import Session, sessionmaker


def session_factory() -> Session:
    SessionDb: Session = sessionmaker(bind=engine)
    return SessionDb()

def commit_on_db(model: SQLModel) -> SQLModel:
    with session_factory() as session:
        session.add(model)
        session.commit()
        session.refresh(model)
        return model