# tests/unit/test_realizar_pedido_service.py

import pytest
from unittest.mock import patch, Mock
import requests

from src.services.realizar_pedido_service import RealizarPedidoService


# ---------- testes _reais_para_centavos_str ----------

def test_reais_para_centavos_str_valor_inteiro():
    service = RealizarPedidoService()
    assert service._reais_para_centavos_str(10.0) == "1000"


def test_reais_para_centavos_str_valor_decimal_arredonda_para_cima():
    service = RealizarPedidoService()
    assert service._reais_para_centavos_str(10.999) == "1100"


def test_reais_para_centavos_str_valor_decimal_arredonda_corretamente():
    service = RealizarPedidoService()
    assert service._reais_para_centavos_str(10.235) == "1024"


def test_reais_para_centavos_str_zero_reais():
    service = RealizarPedidoService()
    assert service._reais_para_centavos_str(0.0) == "0"


# ---------- testes criar_pedido ----------

def test_criar_pedido_monta_payload_correto_e_retorna_resposta():
    service = RealizarPedidoService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = {"status": "ok", "id": 123}

    with patch("src.services.realizar_pedido_service.requests.post", return_value=fake_resp) as mock_post:
        result = service.criar_pedido(
            numero_pedido="1001",
            nome_cliente="João Silva",
            cpf="11122233344",
            comidas=["X-BURGUER", "REFRIGERANTE"],
            preco_total_reais=21.0,
            tempo_preparo_total_min=12,
        )

    mock_post.assert_called_once()
    called_url = (
        mock_post.call_args.kwargs["url"]
        if "url" in mock_post.call_args.kwargs
        else mock_post.call_args.args[0]
    )
    called_json = mock_post.call_args.kwargs["json"]

    assert called_url == "http://127.0.0.1:8000/pedidos"
    assert called_json["NUMERO_PEDIDO"] == "1001"
    assert called_json["NOME_CLIENTE"] == "João Silva"
    assert called_json["CPF"] == "11122233344"
    assert called_json["COMIDAS"] == "X-BURGUER,REFRIGERANTE"
    assert called_json["PRECO"] == "2100"
    assert called_json["TEMPO_PREPARO"] == "12"
    assert result == {"status": "ok", "id": 123}


def test_criar_pedido_retorna_dict_vazio_quando_json_vazio():
    service = RealizarPedidoService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = None

    with patch("src.services.realizar_pedido_service.requests.post", return_value=fake_resp):
        result = service.criar_pedido(
            numero_pedido="1001",
            nome_cliente="João Silva",
            cpf="11122233344",
            comidas=["X-BURGUER"],
            preco_total_reais=10.0,
            tempo_preparo_total_min=5,
        )

    assert result == {}


def test_criar_pedido_propagar_http_error():
    service = RealizarPedidoService()

    fake_resp = Mock()
    fake_resp.raise_for_status.side_effect = requests.HTTPError("Erro 400")
    fake_resp.json.return_value = {}

    with patch("src.services.realizar_pedido_service.requests.post", return_value=fake_resp):
        with pytest.raises(requests.HTTPError):
            service.criar_pedido(
                numero_pedido="1001",
                nome_cliente="João",
                cpf="000",
                comidas=["X"],
                preco_total_reais=1.0,
                tempo_preparo_total_min=1,
            )


def test_criar_pedido_normaliza_numero_pedido_com_zeros_a_esquerda():
    service = RealizarPedidoService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = {"status": "ok"}

    with patch("src.services.realizar_pedido_service.requests.post", return_value=fake_resp) as mock_post:
        service.criar_pedido(
            numero_pedido="0010",
            nome_cliente="Cliente Teste",
            cpf="12345678900",
            comidas=["X-SALADA"],
            preco_total_reais=9.5,
            tempo_preparo_total_min=7,
        )

    called_json = mock_post.call_args.kwargs["json"]
    assert called_json["NUMERO_PEDIDO"] == "10"
    assert called_json["PRECO"] == "950"
    assert called_json["TEMPO_PREPARO"] == "7"


# ---------- testes listar_pedidos_ativos ----------

def test_listar_pedidos_ativos_retorna_lista_quando_json_e_lista():
    service = RealizarPedidoService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = [
        {"id": 1, "NUMERO_PEDIDO": "1001"},
        {"id": 2, "NUMERO_PEDIDO": "1002"},
    ]

    with patch("src.services.realizar_pedido_service.requests.get", return_value=fake_resp) as mock_get:
        result = service.listar_pedidos_ativos()

    mock_get.assert_called_once()
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["NUMERO_PEDIDO"] == "1001"


def test_listar_pedidos_ativos_retorna_lista_vazia_quando_json_nao_e_lista():
    service = RealizarPedidoService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = {"erro": "formato inválido"}

    with patch("src.services.realizar_pedido_service.requests.get", return_value=fake_resp):
        result = service.listar_pedidos_ativos()

    assert result == []


def test_listar_pedidos_ativos_propaga_http_error():
    service = RealizarPedidoService()

    fake_resp = Mock()
    fake_resp.raise_for_status.side_effect = requests.HTTPError("Erro 500")
    fake_resp.json.return_value = []

    with patch("src.services.realizar_pedido_service.requests.get", return_value=fake_resp):
        with pytest.raises(requests.HTTPError):
            service.listar_pedidos_ativos()


def test_listar_pedidos_ativos_quando_json_none_retorna_lista_vazia():
    service = RealizarPedidoService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = None

    with patch("src.services.realizar_pedido_service.requests.get", return_value=fake_resp):
        result = service.listar_pedidos_ativos()

    assert result == []


# ---------- testes atualizar_status_pedidos ----------

def test_atualizar_status_pedidos_retorna_dict_quando_json_e_dict():
    service = RealizarPedidoService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = {"atualizados": 3}

    with patch("src.services.realizar_pedido_service.requests.post", return_value=fake_resp) as mock_post:
        result = service.atualizar_status_pedidos()

    mock_post.assert_called_once()
    assert result == {"atualizados": 3}


def test_atualizar_status_pedidos_retorna_dict_vazio_quando_json_nao_e_dict():
    service = RealizarPedidoService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = ["valor estranho"]

    with patch("src.services.realizar_pedido_service.requests.post", return_value=fake_resp):
        result = service.atualizar_status_pedidos()

    assert result == {}


def test_atualizar_status_pedidos_propaga_http_error():
    service = RealizarPedidoService()

    fake_resp = Mock()
    fake_resp.raise_for_status.side_effect = requests.HTTPError("Erro 503")
    fake_resp.json.return_value = {}

    with patch("src.services.realizar_pedido_service.requests.post", return_value=fake_resp):
        with pytest.raises(requests.HTTPError):
            service.atualizar_status_pedidos()