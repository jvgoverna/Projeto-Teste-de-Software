# src/services/visualizar_historico_service.py
import requests

class HistoricoService:
    BASE_URL = "http://127.0.0.1:8000"

    def listar_historico(self) -> list[dict]:
        resp = requests.get(f"{self.BASE_URL}/pedidos/historico", timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []