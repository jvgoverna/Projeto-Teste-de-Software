import requests

class VisualizarNotasFiscaisService:

    BASE_URL = "http://127.0.0.1:8000"

    def listar_notas_fiscais(self):
        response = requests.get(f"{self.BASE_URL}/notas-fiscais")
        response.raise_for_status()

        data = response.json() or []
        notas_fiscais = []

        for item in data:
            numero_pedido = item.get("NUMERO_PEDIDO", "N/A")
            nome_cliente = item.get("NOME_CLIENTE", "N/A")
            cpf = item.get("CPF", "N/A")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            notas_fiscais.append({
                "NUMERO_PEDIDO": numero_pedido,
                "NOME_CLIENTE": nome_cliente,
                "CPF": cpf,
                "PRECO": preco_reais
            })
        return notas_fiscais
    """

    Exemplo
    --------
    GET /notas-fiscais

    Resposta (200):
    [
      { "id": 1, "NUMERO_PEDIDO": "1001", "NOME_CLIENTE": "João Silva", "CPF": "11122233344", "PRECO": "2100" },
      { "id": 2, "NUMERO_PEDIDO": "1002", "NOME_CLIENTE": "Maria Oliveira", "CPF": "99988877766", "PRECO": "1700" }
    ]
    """