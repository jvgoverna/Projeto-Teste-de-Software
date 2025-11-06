import requests

class VisualizarCardapioService:
    BASE_URL = "http://127.0.0.1:8000"

    def view_menu(self):
        response = requests.get(f"{self.BASE_URL}/cardapio/unidade")
        response.raise_for_status()

        data = response.json() or []
        itens = []

        for item in data:
            comida = item.get("COMIDA", "Sem nome")
            preco_centavos = item.get("PRECO", "0")
            try:
                preco_reais = int(preco_centavos) / 100
            except (ValueError, TypeError):
                preco_reais = 0.0

            tempo = item.get("TEMPO_PREPARO", "N/A")
            itens.append({"nome": comida, "preco": preco_reais, "tempo_preparo": tempo})

        return itens
