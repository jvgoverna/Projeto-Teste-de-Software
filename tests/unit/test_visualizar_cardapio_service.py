# tests/unit/test_visualizar_cardapio_service.py

import pytest
from unittest.mock import patch, Mock

from services.visualizar_cardapio_service import VisualizarCardapioService


def test_view_menu_fluxo_feliz_conversao_preco():
    service = VisualizarCardapioService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = [
        {"COMIDA": "X-BURGUER", "PRECO": "2100", "TEMPO_PREPARO": "12"},
        {"COMIDA": "REFRIGERANTE", "PRECO": "500", "TEMPO_PREPARO": "0"},
    ]

    with patch("services.visualizar_cardapio_service.requests.get", return_value=fake_resp):
        itens = service.view_menu()

    assert len(itens) == 2
    assert itens[0] == {"nome": "X-BURGUER", "preco": 21.0, "tempo_preparo": "12"}
    assert itens[1] == {"nome": "REFRIGERANTE", "preco": 5.0, "tempo_preparo": "0"}


def test_view_menu_dados_invalidos_usa_defaults():
    service = VisualizarCardapioService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = [
        {"PRECO": "abc", "TEMPO_PREPARO": "10"},          # sem COMIDA, PRECO inválido
        {"COMIDA": "Batata Frita", "PRECO": None},        # PRECO None
        {},                                               # tudo faltando
    ]

    with patch("services.visualizar_cardapio_service.requests.get", return_value=fake_resp):
        itens = service.view_menu()

    assert len(itens) == 3

    assert itens[0]["nome"] == "Sem nome"
    assert itens[0]["preco"] == 0.0
    assert itens[0]["tempo_preparo"] == "10"

    assert itens[1]["nome"] == "Batata Frita"
    assert itens[1]["preco"] == 0.0

    assert itens[2]["nome"] == "Sem nome"
    assert itens[2]["preco"] == 0.0
    assert itens[2]["tempo_preparo"] == "N/A"