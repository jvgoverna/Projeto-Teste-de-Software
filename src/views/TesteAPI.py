"""
EXEMPLOS DE CONSUMO DA API — BurgerFeiAPI
=========================================

Requisitos:
-----------
pip install requests

Como usar:
----------
1) Certifique-se que o servidor está rodando:
   uvicorn Server.BurgerFeiAPI:app --reload --port 8000
2) Execute este script:
   python api_examples.py
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"


# =====================================================
# 🧩 INFRA
# =====================================================

def testar_infra():
    print("\n=== TESTES INFRA ===")

    # 1) Health check
    resp = requests.get(f"{BASE_URL}/health")
    print("GET /health →", resp.status_code, resp.json())

    # 2) Ping banco
    resp = requests.get(f"{BASE_URL}/db/ping")
    print("GET /db/ping →", resp.status_code, resp.json())

    # 3) Dump do banco (debug)
    resp = requests.get(f"{BASE_URL}/_debug/db/dump")
    print("GET /_debug/db/dump →", resp.status_code)
    print(json.dumps(resp.json(), indent=2, ensure_ascii=False))


# =====================================================
# 🍔 CARDÁPIO
# =====================================================

def testar_cardapio():
    print("\n=== TESTES CARDÁPIO ===")

    # 1) Listar cardápio central
    resp = requests.get(f"{BASE_URL}/cardapio/central")
    print("GET /cardapio/central →", resp.status_code)
    print(json.dumps(resp.json(), indent=2, ensure_ascii=False))

    # 2) Ativar itens no cardápio da unidade
    body_ativar = { "itens": [1, 2, 3] }
    resp = requests.post(f"{BASE_URL}/cardapio/unidade/itens", json=body_ativar)
    print("POST /cardapio/unidade/itens →", resp.status_code, resp.json())

    # 3) Atualizar itens no cardápio da unidade
    body_atualizar = {
        "itens": [
            {"id": 3, "PRECO": "1800"},
            {"id": 5, "TEMPO_PREPARO": "9"}
        ]
    }
    resp = requests.put(f"{BASE_URL}/cardapio/unidade/itens", json=body_atualizar)
    print("PUT /cardapio/unidade/itens →", resp.status_code)
    print(json.dumps(resp.json(), indent=2, ensure_ascii=False))

    # 4) Remover itens do cardápio da unidade
    body_remover = { "itens": [1, 4] }
    resp = requests.delete(f"{BASE_URL}/cardapio/unidade/itens", json=body_remover)
    print("DELETE /cardapio/unidade/itens →", resp.status_code, resp.json())

    # 5) Listar cardápio da unidade (depois das alterações)
    resp = requests.get(f"{BASE_URL}/cardapio/unidade")
    print("GET /cardapio/unidade →", resp.status_code)
    print(json.dumps(resp.json(), indent=2, ensure_ascii=False))


# =====================================================
# 🧾 PEDIDOS
# =====================================================

def testar_pedidos():
    print("\n=== TESTES PEDIDOS ===")

    # 1) Criar um pedido (gera nota fiscal automaticamente)
    body_pedido = {
        "NUMERO_PEDIDO": "1003",
        "NOME_CLIENTE": "Carlos Mendes",
        "CPF": "11122233344",
        "COMIDAS": "HAMBURGUER, REFRIGERANTE",
        "PRECO": "2100",
        "TEMPO_PREPARO": "11"
    }
    resp = requests.post(f"{BASE_URL}/pedidos", json=body_pedido)
    print("POST /pedidos →", resp.status_code)
    print(json.dumps(resp.json(), indent=2, ensure_ascii=False))

    # 2) Listar pedidos ativos
    resp = requests.get(f"{BASE_URL}/pedidos/ativos")
    print("GET /pedidos/ativos →", resp.status_code)
    print(json.dumps(resp.json(), indent=2, ensure_ascii=False))

    # 3) Atualizar status (move prontos para histórico)
    resp = requests.post(f"{BASE_URL}/pedidos/atualizar-status")
    print("POST /pedidos/atualizar-status →", resp.status_code)
    print(json.dumps(resp.json(), indent=2, ensure_ascii=False))

    # 4) Listar histórico de pedidos
    resp = requests.get(f"{BASE_URL}/pedidos/historico")
    print("GET /pedidos/historico →", resp.status_code)
    print(json.dumps(resp.json(), indent=2, ensure_ascii=False))

    # 5) Listar notas fiscais
    resp = requests.get(f"{BASE_URL}/notas_fiscais")
    print("GET /notas_fiscais →", resp.status_code)
    print(json.dumps(resp.json(), indent=2, ensure_ascii=False))


# =====================================================
# 🚀 EXECUTAR TUDO
# =====================================================

if __name__ == "__main__":
    testar_infra()
    testar_cardapio()
    testar_pedidos()