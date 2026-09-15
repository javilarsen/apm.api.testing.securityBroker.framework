import pytest
from typing import List
from models.product import ProductResponse

class TestProducts:

    @pytest.mark.smoke
    def test_get_all_products_success(self, product_service):
        # Act: Llamada a la API local de APM Security Broker
        response = product_service.get_all_products()

        # Assert 1: Código de respuesta exitoso (200 OK)
        assert response.status_code == 200, f"Se esperaba 200 pero fue {response.status_code}"

        # Assert 2: Validar el contrato de respuesta contra la lista de productos de Pydantic
        json_data = response.json()
        assert isinstance(json_data, list), "La respuesta debe ser una lista de productos"
        
        # Convierte la respuesta JSON a objetos ProductResponse
        products = [ProductResponse(**item) for item in json_data]

        # Valida que traiga al menos un elemento o que respete los tipos si hay datos
        if len(products) > 0:
            assert products[0].productId is not None
            assert isinstance(products[0].productName, str)
            assert isinstance(products[0].isActive, bool)