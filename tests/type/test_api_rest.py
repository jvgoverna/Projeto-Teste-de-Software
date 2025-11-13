# tests/type/test_api_rest.py

import time
import requests

BASE_URL = "http://127.0.0.1:8000"


def test_health_endpoint_retorna_ok():
    resp = requests.get(f"{BASE_URL}/health", timeout=5)

    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_get_cardapio_central_retorna_lista():
    resp = requests.get(f"{BASE_URL}/cardapio/central", timeout=5)

    assert resp.status_code == 200
    data = resp.json()

    assert isinstance(data, list)
    if data:
        assert "COMIDA" in data[0]
        assert "PRECO" in data[0]
        assert "TEMPO_PREPARO" in data[0]


def test_post_pedidos_cria_pedido_e_retorna_201():
    numero_pedido = str(int(time.time()))  # só para ser único

    payload = {
        "NUMERO_PEDIDO": numero_pedido,
        "NOME_CLIENTE": "Teste API",
        "CPF": "11122233344",
        "COMIDAS": "X-BURGUER, REFRIGERANTE",
        "PRECO": "2100",
        "TEMPO_PREPARO": "5",
    }

    resp = requests.post(f"{BASE_URL}/pedidos", json=payload, timeout=5)
    assert resp.status_code == 201

    data = resp.json()
    assert "id_pedido_inserido" in data
    assert "id_nota_fiscal_inserida" in data
    assert data["mensagem"].startswith("Pedido")


def test_cardapio_unidade_ativar_item_e_listar():
    # pega um item do cardápio central
    resp_central = requests.get(f"{BASE_URL}/cardapio/central", timeout=5)
    assert resp_central.status_code == 200

    central = resp_central.json()
    assert isinstance(central, list)
    assert len(central) > 0

    id_para_ativar = central[0]["id"]

    # ativa na unidade
    resp_post = requests.post(
        f"{BASE_URL}/cardapio/unidade/itens",
        json={"itens": [id_para_ativar]},
        timeout=5,
    )
    assert resp_post.status_code == 200
    body = resp_post.json()
    assert body["quantidade_de_itens_ativados"] >= 1

    # lista a unidade
    resp_unidade = requests.get(f"{BASE_URL}/cardapio/unidade", timeout=5)
    assert resp_unidade.status_code == 200
    unidade = resp_unidade.json()
    assert isinstance(unidade, list)
    assert len(unidade) >= 1


def test_cardapio_unidade_ativar_body_invalido_retorna_422():
    """
    Aqui o FastAPI/Pydantic faz a validação de tipos:
    - a rota espera List[int]
    - estamos mandando ["a", "b", "c"]
    Resultado: 422 Unprocessable Entity (antes de entrar na função).
    """
    resp = requests.post(
        f"{BASE_URL}/cardapio/unidade/itens",
        json={"itens": ["a", "b", "c"]},
        timeout=5,
    )

    assert resp.status_code == 422
    data = resp.json()
    assert "detail" in data
    assert isinstance(data["detail"], list)


def test_delete_cardapio_unidade_remove_item():
    # garante item na unidade: ativa um do cardápio central
    central_resp = requests.get(f"{BASE_URL}/cardapio/central", timeout=5)
    assert central_resp.status_code == 200
    central = central_resp.json()
    assert central

    id_central = central[0]["id"]

    post_resp = requests.post(
        f"{BASE_URL}/cardapio/unidade/itens",
        json={"itens": [id_central]},
        timeout=5,
    )
    assert post_resp.status_code == 200

    unidade_resp = requests.get(f"{BASE_URL}/cardapio/unidade", timeout=5)
    assert unidade_resp.status_code == 200
    unidade = unidade_resp.json()
    assert unidade

    id_unidade = unidade[-1]["id"]

    delete_resp = requests.delete(
        f"{BASE_URL}/cardapio/unidade/itens",
        json={"itens": [id_unidade]},
        timeout=5,
    )

    assert delete_resp.status_code == 200
    body = delete_resp.json()
    assert body["quantidade_de_itens_removidos"] >= 1
    assert isinstance(body["lista_de_erros_durante_remocao"], list)