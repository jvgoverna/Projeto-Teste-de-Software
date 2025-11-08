import requests
class RealizarPedidoService:
    BASE_URL = "http://127.0.0.1:8000"

    @staticmethod
    def _reais_para_centavos_str(valor_reais: float) -> str:
        return str(int(round(valor_reais * 100)))

    def criar_pedido(self, numero_pedido: str, nome_cliente: str, cpf: str,
                     comidas: list[str], preco_total_reais: float,
                     tempo_preparo_total_min: int) -> dict:
        payload = {
            "NUMERO_PEDIDO": str(int(numero_pedido)),
            "NOME_CLIENTE": nome_cliente,
            "CPF": cpf,
            "COMIDAS": ",".join(comidas),
            "PRECO": self._reais_para_centavos_str(preco_total_reais),
            "TEMPO_PREPARO": str(int(tempo_preparo_total_min)),
        }

        resp = requests.post(f"{self.BASE_URL}/pedidos", json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json() or {}
    
    def listar_pedidos_ativos(self) -> list[dict]:
        """Chama GET /pedidos/ativos e retorna a lista de pedidos em preparo."""
        resp = requests.get(f"{self.BASE_URL}/pedidos/ativos", timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def atualizar_status_pedidos(self) -> dict:
        resp = requests.post(f"{self.BASE_URL}/pedidos/atualizar-status", timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, dict) else {}