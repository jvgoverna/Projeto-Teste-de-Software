import requests

class PedidosFilaService:
    
    BASE_URL = "http://127.0.0.1:8000"

    def listar_pedidos_ativos(self) -> list[dict]:
        """Chama GET /pedidos/ativos e retorna a lista de pedidos em preparo."""
        resp = requests.get(f"{self.BASE_URL}/pedidos/ativos", timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []