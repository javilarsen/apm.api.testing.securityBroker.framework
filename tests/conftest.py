import pytest
from services.product_service import ProductService
from db.database import DatabaseClient

@pytest.fixture
def product_service():
    return ProductService()

@pytest.fixture(scope="session")
def db_client():
    return DatabaseClient()