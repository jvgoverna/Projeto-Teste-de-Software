import pytest
import requests

from codigo.services.realizar_pedido_service import RealizarPedidoService
from types import SimpleNamespace

service = RealizarPedidoService()
chamado = {}

def test_reais_para_centavos_str():

    assert service._reais_para_centavos_str(21.00) == "2100"
    assert service._reais_para_centavos_str(10.34) == "1034"
    assert service._reais_para_centavos_str(0.0) == "0"

def fake_post(url, json, timeout):
    chamado["url"] = url
    chamado["json"] = json
    chamado["timeout"] = timeout

    # objeto simples com os métodos usados na service
    return SimpleNamespace(
        raise_for_status=lambda: None,
        json=lambda: {"ok": True, "id": 123}
    )

def fake_post_vazio(url, json, timeout=10):
    return SimpleNamespace(
        raise_for_status=lambda: None,
        json=lambda: None
    )

def fake_post_status(url, timeout=10):

    return SimpleNamespace(
        raise_for_status=lambda: None,
        json=lambda: {"atualizados": 3}
    )

def test_criar_pedido(monkeypatch):
    # troca o requests.post da service pelo fake_post
    monkeypatch.setattr(
        "src.services.realizar_pedido_service.requests.post",
        fake_post,
    )

    resultado = service.criar_pedido(
        numero_pedido="1001",
        nome_cliente="João Silva",
        cpf="12345678900",
        comidas=["HAMBURGUER", "REFRIGERANTE"],
        preco_total_reais=21.00,
        tempo_preparo_total_min=11,
    )

    # verifica retorno
    assert resultado == {"ok": True, "id": 123}

    # verifica dados básicos enviados
    payload = chamado["json"]
    assert payload["NUMERO_PEDIDO"] == "1001"
    assert payload["COMIDAS"] == "HAMBURGUER,REFRIGERANTE"
    assert payload["PRECO"] == "2100"  # 21.00 -> 2100

def test_criar_pedido_resposta_vazia(monkeypatch):

    monkeypatch.setattr(
        "src.services.realizar_pedido_service.requests.post",
        fake_post_vazio,
    )

    result = service.criar_pedido(
        numero_pedido="1002",
        nome_cliente="Maria",
        cpf="00000000000",
        comidas=[],
        preco_total_reais=0.0,
        tempo_preparo_total_min=0,
    )

    assert result == {}  # caiu no "or {}"



def test_atualizar_status_pedidos(monkeypatch):
    # troca o requests.post dentro da service pelo fake_post_status
    monkeypatch.setattr(
        "src.services.realizar_pedido_service.requests.post",
        fake_post_status,
    )

    resultado = service.atualizar_status_pedidos()

    assert resultado == {"atualizados": 3}