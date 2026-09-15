import pytest
from services.product_service import ProductService

@pytest.fixture
def product_service():
    return ProductService()