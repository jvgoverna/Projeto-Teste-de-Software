# tests/unit/test_visualizar_notas_fiscais_service.py

import pytest
from unittest.mock import patch, Mock

from src.services.visualizar_notas_fiscais_service import VisualizarNotasFiscaisService


def test_listar_notas_fiscais_fluxo_feliz_conversao_preco():
    service = VisualizarNotasFiscaisService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = [
        {
            "id": 1,
            "NUMERO_PEDIDO": "1001",
            "NOME_CLIENTE": "João Silva",
            "CPF": "11122233344",
            "PRECO": "2100",
        },
        {
            "id": 2,
            "NUMERO_PEDIDO": "1002",
            "NOME_CLIENTE": "Maria Oliveira",
            "CPF": "99988877766",
            "PRECO": "1700",
        },
    ]

    with patch("src.services.visualizar_notas_fiscais_service.requests.get", return_value=fake_resp):
        notas = service.listar_notas_fiscais()

    assert len(notas) == 2

    assert notas[0]["NUMERO_PEDIDO"] == "1001"
    assert notas[0]["NOME_CLIENTE"] == "João Silva"
    assert notas[0]["CPF"] == "11122233344"
    assert notas[0]["PRECO"] == 21.0

    assert notas[1]["NUMERO_PEDIDO"] == "1002"
    assert notas[1]["NOME_CLIENTE"] == "Maria Oliveira"
    assert notas[1]["CPF"] == "99988877766"
    assert notas[1]["PRECO"] == 17.0

def test_listar_notas_fiscais_dados_invalidos_usa_defaults():
    service = VisualizarNotasFiscaisService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = [
        {
            "NUMERO_PEDIDO": "2001",
            "NOME_CLIENTE": "Cliente Bugado",
            "CPF": "00000000000",
            "PRECO": "abc",        # inválido
        },
        {
            # sem NUMERO_PEDIDO / NOME_CLIENTE / CPF / PRECO
        },
    ]

    with patch("src.services.visualizar_notas_fiscais_service.requests.get", return_value=fake_resp):
        notas = service.listar_notas_fiscais()

    assert len(notas) == 2

    # Primeiro: tem número, nome, cpf, mas preço inválido ⇒ 0.0
    assert notas[0]["NUMERO_PEDIDO"] == "2001"
    assert notas[0]["NOME_CLIENTE"] == "Cliente Bugado"
    assert notas[0]["CPF"] == "00000000000"
    assert notas[0]["PRECO"] == 0.0

    # Segundo: tudo default
    assert notas[1]["NUMERO_PEDIDO"] == "N/A"
    assert notas[1]["NOME_CLIENTE"] == "N/A"
    assert notas[1]["CPF"] == "N/A"
    assert notas[1]["PRECO"] == 0.0