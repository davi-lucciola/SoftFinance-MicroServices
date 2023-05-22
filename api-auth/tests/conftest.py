import pytest
from app.main import api_auth
from collections.abc import Generator
from fastapi.testclient import TestClient


@pytest.fixture(scope="function")
def client() -> Generator:
    with TestClient(api_auth) as api:
        yield api