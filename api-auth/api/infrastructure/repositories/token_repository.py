from sqlmodel import select
from ...domain.models import Token
from ..connection.session import commit_on_db, session_factory


def get_by_user_id(user_id: int) -> list[Token] | None:
    with session_factory() as session:
        token: list[Token] = session.execute (
            select(Token).where(Token.user_id == user_id)
        ).all()
        return token if len(token) > 0 else None

def get_by_acess_token(acess_token: str) -> list[Token]  | None:
    with session_factory() as session:
        token: list[Token] = session.execute (
            select(Token).where(Token.acess_token == acess_token)
        ).all()
        return token if len(token) > 0 else None

def save_token(token: Token) -> Token:
    return commit_on_db(token)