from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Encuentra la raíz de la carpeta del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    # Configuración de la API y la base de datos
    BASE_URL: str
    DB_CONNECTION_STRING: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8"
    )

settings = Settings()