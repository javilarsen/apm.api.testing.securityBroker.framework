import requests
import urllib3
from config.settings import settings

# Desactivar las advertencias de SSL inseguro en la consola
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class BaseClient:
    def __init__(self, base_url: str = settings.BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        # Desactiva la verificación de certificado para localhost
        self.session.verify = False
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        return self.session.request(method, url, **kwargs)

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("POST", endpoint, **kwargs)