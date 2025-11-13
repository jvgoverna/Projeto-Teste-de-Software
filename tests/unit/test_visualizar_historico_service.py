import pytest
from unittest.mock import patch
import requests

from services.visualizar_historico_service import HistoricoService


def test_listar_historico_fluxo_feliz():
    """
    Simula o servidor respondendo corretamente com uma lista de pedidos históricos.
    """

    fake_response = type("FakeResponse", (), {})()

    def fake_raise():
        pass

    fake_response.raise_for_status = fake_raise

    def fake_json():
        return [
            {
                "id": 1,
                "NUMERO_PEDIDO": "2001",
                "NOME_CLIENTE": "Maria Oliveira",
                "CPF": "99988877766",
                "COMIDAS": "X-Bacon, Refrigerante",
                "PRECO": "3200",
                "TEMPO_PREPARO": "15",
                "HORARIO_ADICIONADO": "1730473100"
            }
        ]

    fake_response.json = fake_json

    with patch("requests.get", return_value=fake_response):
        service = HistoricoService()
        resultado = service.listar_historico()

    assert len(resultado) == 1
    assert resultado[0]["NOME_CLIENTE"] == "Maria Oliveira"
    assert resultado[0]["NUMERO_PEDIDO"] == "2001"

def test_listar_historico_quando_servidor_retorna_erro():
    """
    Simula erro do servidor.
    """

    fake_response = type("FakeResponse", (), {})()

    def fake_raise():
        raise requests.HTTPError("Erro 500 - Histórico indisponível")

    fake_response.raise_for_status = fake_raise

    fake_response.json = lambda: []

    with patch("requests.get", return_value=fake_response):
        service = HistoricoService()

        with pytest.raises(requests.HTTPError):
            service.listar_historico()