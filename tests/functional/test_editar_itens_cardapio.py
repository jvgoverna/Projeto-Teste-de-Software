from types import SimpleNamespace
from src.services.editar_itens_cardapio_service import EditarItensCardapioService

import pytest

chamado_ativar = {}
service = EditarItensCardapioService()

def fake_get_cardapio(url, timeout=10):
    return SimpleNamespace(
        raise_for_status=lambda: None,
        json=lambda: [
            {
                "id": 1,
                "COMIDA": "HAMBURGUER",
                "PRECO": "1700",
                "TEMPO_PREPARO": "8",
            },
            {
                "id": 3,
                "COMIDA": "BATATA_FRITA",
                "PRECO": "1800",
                "TEMPO_PREPARO": "5",
            },
        ],
    )


def fake_post_ativar(url,json,timeout=10):
    chamado_ativar["url"] = url
    chamado_ativar["json"] = json
    chamado_ativar["timeout"] = timeout

    return SimpleNamespace(
        raise_for_status=lambda: None,
        json=lambda: {
            "quantidade_de_itens_ativados": 3,
            "lista_de_erros_durante_ativacao": [
                {
                    "id": "6",
                    "erro": "Item não encontrado no CARDAPIO_CENTRAL",
                }
            ],
        },
    )

def fake_delete_cardapio_unidade(url,json):
    chamado_ativar["url"] = url
    chamado_ativar["json"] = json

    return SimpleNamespace(
        raise_for_status=lambda: None,
        json=lambda: {
            "quantidade_de_itens_removidos" : 2,
            "lista_de_erros_durante_remocao":[
                {
                    "id": "6",
                    "erro":"Falha ao remover do CARDAPIO_UNIDADE"
                }
            ]
        },

    )


def test_listar_cardapio_unidade(monkeypatch):
    monkeypatch.setattr(
        "src.services.editar_itens_cardapio_service.requests.get",
        fake_get_cardapio,
    )

    resultado = service.listar_cardapio_unidade()

    assert resultado == [
        {"id": 1,"COMIDA": "HAMBURGUER", "PRECO": "1700", "TEMPO_PREPARO": "8"},
        {"id": 3,"COMIDA": "BATATA_FRITA", "PRECO": "1800", "TEMPO_PREPARO": "5"},
    ]

def test_listar_cardapio_central(monkeypatch):
    monkeypatch.setattr(
        "src.services.editar_itens_cardapio_service.requests.get",
        fake_get_cardapio,
    )

    resultado = service.listar_cardapio_central()

    assert resultado == [
        {"id": 1,"COMIDA": "HAMBURGUER", "PRECO": "1700", "TEMPO_PREPARO": "8"},
        {"id": 3,"COMIDA": "BATATA_FRITA", "PRECO": "1800", "TEMPO_PREPARO": "5"},
    ]

def test_ativar_itens_cardapio_unidade(monkeypatch):

    monkeypatch.setattr(
        "src.services.editar_itens_cardapio_service.requests.post",
        fake_post_ativar,
    )

    # mistura de valores que viram int com alguns "lixos"
    resultado = service.ativar_itens_cardapio_unidade([1, "2", None, "aA"])

    assert resultado == []

    # conferindo se o payload foi montado certo
    payload = chamado_ativar["json"]
    assert payload == {"itens": [1, 2]}  # só os válidos entram

    # confere URL e timeout
    assert chamado_ativar["url"].endswith("/cardapio/unidade/itens")
    assert chamado_ativar["timeout"] == 10

def test_ativar_itens_cardapio_unidade_lista_vazia():

    with pytest.raises(ValueError, match="lista de IDs não pode ser vazia"):
        service.ativar_itens_cardapio_unidade([])


def test_ativar_itens_cardapio_unidade_ID_invalido():

    with pytest.raises(ValueError, match="Nenhum ID válido foi informado."):
        service.ativar_itens_cardapio_unidade([None,"","abc"])


def test_remover_itens_cardapio_unidade(monkeypatch):
    monkeypatch.setattr(
        "src.services.editar_itens_cardapio_service.requests.delete",
        fake_delete_cardapio_unidade,
    )

    resultado = service.remover_itens_cardapio_unidade([1, "2", None, "aA"])

    assert resultado == []

    # conferindo se o payload foi montado certo
    payload = chamado_ativar["json"]
    assert payload == {"itens": [1, 2]}  # só os válidos entram

    # confere URL e timeout
    assert chamado_ativar["url"].endswith("/cardapio/unidade/itens")
    assert chamado_ativar["timeout"] == 10


def test_remover_itens_cardapio_unidade_lista_vazia():
    with pytest.raises(ValueError, match="lista de IDs não pode ser vazia"):
        service.remover_itens_cardapio_unidade([])

def test_remover_itens_cardapio_unidade_ID_invalido():

    with pytest.raises(ValueError, match="Nenhum ID válido foi informado."):
        service.remover_itens_cardapio_unidade([None,"","abc"])