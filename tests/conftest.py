import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def mock_db():

    return MagicMock()


@pytest.fixture
def client():

    return TestClient(app)