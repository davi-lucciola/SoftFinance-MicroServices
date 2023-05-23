from fastapi import FastAPI
from .controllers import card_controller
from .infrastructure.connection import create_tables


def create_app(title: str, description: str) -> FastAPI:
    app = FastAPI (
        title = title,
        description = description
    )

    app = include_routers(app)

def include_routers(app: FastAPI) -> FastAPI:
    app.include_router(card_controller.router)
    return app

def init_db(app: FastAPI) -> FastAPI:
    
    @app.on_event('startup')
    def startup() -> None:
        create_tables()

    return app