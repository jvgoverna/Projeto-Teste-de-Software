import requests
import json

class VisualizarCardapioService:
    BASE_URL = "http://127.0.0.1:8000"

    def view_menu(self):

        try:
            response = requests.get(f"{self.BASE_URL}/cardapio/unidade")

            if response.status_code != 200:
                print(f"❌ Erro ao obter cardápio (status {response.status_code})")
                return

            data = response.json()

            if not data:
                print("⚠️ Nenhum produto encontrado no cardápio.")
                return

            print("┌" + "─" * 52 + "┐")
            print("│{:^52}│".format("CARDÁPIO DA UNIDADE"))
            print("├" + "─" * 52 + "┤")

            for item in data:
                comida = item.get("COMIDA", "Sem nome")
                preco_centavos = item.get("PRECO", "0")

                # Converter preço (string em centavos) para float (reais)
                try:
                    preco_reais = int(preco_centavos) / 100
                except ValueError:
                    preco_reais = 0.0

                tempo = item.get("TEMPO_PREPARO", "N/A")

                # Exibir linha formatada
                print(f"│ {comida:<30} R$ {preco_reais:>6.2f}   ({tempo} min) │")

            print("└" + "─" * 52 + "┘\n")

        except requests.exceptions.RequestException as e:
            print("❌ Erro de conexão com o servidor:")
            print(e)
