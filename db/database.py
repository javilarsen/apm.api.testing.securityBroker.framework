
from sqlalchemy import create_engine, text
from config.settings import settings

class DatabaseClient:
    def __init__(self):
        # Utiliza la variable declarada en config/settings.py
        self.engine = create_engine(settings.DB_CONNECTION_STRING)

    def execute_query(self, query: str, params: dict = None):
        """Ejecuta una consulta SQL SELECT y devuelve los resultados como lista de diccionarios"""
        with self.engine.connect() as connection:
            result = connection.execute(text(query), params or {})
            return [dict(row._mapping) for row in result]