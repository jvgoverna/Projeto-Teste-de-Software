from types import SimpleNamespace
from src.services.visualizar_cardapio_service import VisualizarCardapioService

import pytest

service = VisualizarCardapioService()

from types import SimpleNamespace
from src.services.visualizar_cardapio_service import VisualizarCardapioService

service = VisualizarCardapioService()


def fake_visualizar_itens_cardapio(url, timeout=10):
    return SimpleNamespace(
        raise_for_status=lambda: None,
        json=lambda: [
            {
                "id": 3,
                "COMIDA": "MILKSHAKE",
                "PRECO": "1500",
                "TEMPO_PREPARO": "4",
            }
        ],
    )

def fake_visualizar_itens_cardapio_preco_invalido(url, timeout=10):
    return SimpleNamespace(
        raise_for_status=lambda: None,
        json=lambda: [
            {
                "id": 3,
                "COMIDA": "MILKSHAKE",
                "PRECO": "aa",
                "TEMPO_PREPARO": "4",
            }
        ],
    )


def test_view_menu(monkeypatch):
    monkeypatch.setattr(
        "src.services.visualizar_cardapio_service.requests.get",
        fake_visualizar_itens_cardapio,
    )

    resultado = service.view_menu()

    assert resultado == [
        {"nome": "MILKSHAKE", "preco": 15.0, "tempo_preparo": "4"},
    ]

def test_view_menu_preco_zerado(monkeypatch):

    monkeypatch.setattr(
        "src.services.visualizar_cardapio_service.requests.get",
        fake_visualizar_itens_cardapio_preco_invalido,
    )

    resultado = service.view_menu()

    assert resultado == [
        {"nome": "MILKSHAKE", "preco": 0.0, "tempo_preparo": "4"},
    ]
