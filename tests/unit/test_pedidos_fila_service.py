import pytest
from unittest.mock import patch

from src.services.pedidos_fila_service import PedidosFilaService
import requests


def test_listar_pedidos_ativos_retorna_lista_valida():
    """
    Este teste simula o servidor respondendo corretamente com um pedido ativo.
    """

    fake_response = type("FakeResponse", (), {})()   # cria um objeto vazio

    def fake_raise():
        pass

    fake_response.raise_for_status = fake_raise

    def fake_json():
        return [
            {
                "id": 1,
                "NUMERO_PEDIDO": "1001",
                "NOME_CLIENTE": "João Silva",
                "CPF": "11122233344",
                "COMIDAS": "X-BURGUER, REFRIGERANTE",
                "PRECO": "2100",
                "TEMPO_PREPARO": "12",
                "HORARIO_ADICIONADO": "1730472103"
            }
        ]

    fake_response.json = fake_json

    with patch("requests.get", return_value=fake_response):
        service = PedidosFilaService()
        resultado = service.listar_pedidos_ativos()

    assert resultado[0]["NOME_CLIENTE"] == "João Silva"
    assert resultado[0]["NUMERO_PEDIDO"] == "1001"
    assert resultado[0]["COMIDAS"] == "X-BURGUER, REFRIGERANTE"


def test_listar_pedidos_ativos_quando_servidor_retorna_erro():
    """
    Simula o servidor retornando erro HTTP.
    """

    fake_response = type("FakeResponse", (), {})()

    def fake_raise():
        raise requests.HTTPError("Erro 500 no servidor")

    fake_response.raise_for_status = fake_raise

    fake_response.json = lambda: []

    # substitui requests.get para devolverfake
    with patch("requests.get", return_value=fake_response):
        service = PedidosFilaService()

        with pytest.raises(requests.HTTPError):
            service.listar_pedidos_ativos()