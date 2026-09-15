import requests
from services.base_client import BaseClient

class ProductService(BaseClient):
    def __init__(self):
        super().__init__()
        self.ENDPOINT = "/api/products"

    def get_all_products(self) -> requests.Response:
        return self.get(self.ENDPOINT)