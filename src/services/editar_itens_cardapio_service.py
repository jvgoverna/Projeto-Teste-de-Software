import requests

class EditarItensCardapioService:
    
    BASE_URL = "http://127.0.0.1:8000"

    def listar_cardapio_unidade(self) -> dict:
        """Retorna os itens atualmente ativos e disponíveis para venda na unidade."""
        resp = requests.get(f"{self.BASE_URL}/cardapio/unidade", timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def ativar_itens_cardapio_unidade(self, ids: list[int]) -> dict:

        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.post(f"{self.BASE_URL}/cardapio/unidade/itens",json=payloads,timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
    
    def remover_itens_cardapio_unidade(self, ids: list[int]) -> dict:
        if not ids:
            raise ValueError("A lista de IDs não pode ser vazia.")
        

        payloads = {
            "itens": []
        }
        
        #Garante inteiros  (ignora nulos/vazios)
        for x in ids:
            try:
                payloads["itens"].append(int(x))
            except (TypeError, ValueError):
                pass

        if not payloads["itens"]:
            raise ValueError("Nenhum ID válido foi informado.")


        resp = requests.delete(f"{self.BASE_URL}/cardapio/unidade/itens", json=payloads)

        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []


    def listar_cardapio_central(self) -> dict:
        resp = requests.get(f"{self.BASE_URL}/cardapio/central")
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []
