import pytest
from unittest.mock import patch, Mock
import requests

from src.services.editar_itens_cardapio_service import EditarItensCardapioService


# ---------- listar_cardapio_unidade ----------

def test_listar_cardapio_unidade_retorna_lista_quando_json_e_lista():
    service = EditarItensCardapioService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = [
        {"id": 10, "COMIDA": "X-Salada"},
        {"id": 20, "COMIDA": "X-Burger"},
    ]

    with patch("src.services.editar_itens_cardapio_service.requests.get", return_value=fake_resp) as mock_get:
        resultado = service.listar_cardapio_unidade()

    mock_get.assert_called_once_with("http://127.0.0.1:8000/cardapio/unidade", timeout=10)
    assert isinstance(resultado, list)
    assert len(resultado) == 2
    assert resultado[0]["COMIDA"] == "X-Salada"


def test_listar_cardapio_unidade_retorna_lista_vazia_quando_json_nao_e_lista():
    service = EditarItensCardapioService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = {"erro": "formato inválido"}

    with patch("src.services.editar_itens_cardapio_service.requests.get", return_value=fake_resp):
        resultado = service.listar_cardapio_unidade()

    assert resultado == []


def test_listar_cardapio_unidade_propaga_http_error():
    service = EditarItensCardapioService()

    fake_resp = Mock()
    fake_resp.raise_for_status.side_effect = requests.HTTPError("Erro 500")
    fake_resp.json.return_value = []

    with patch("src.services.editar_itens_cardapio_service.requests.get", return_value=fake_resp):
        with pytest.raises(requests.HTTPError):
            service.listar_cardapio_unidade()


# ---------- ativar_itens_cardapio_unidade ----------

@pytest.mark.parametrize(
    "ids, mensagem_erro",
    [
        ([], "A lista de IDs não pode ser vazia"),
        (["a", None, "xyz"], "Nenhum ID válido foi informado"),
    ],
)
def test_ativar_itens_cardapio_unidade_validacoes_ids(ids, mensagem_erro):
    """
    Teste parametrizado para validar os cenários de erro de IDs:
    - Lista vazia
    - Todos os IDs inválidos
    """
    service = EditarItensCardapioService()

    with pytest.raises(ValueError, match=mensagem_erro):
        service.ativar_itens_cardapio_unidade(ids)


def test_ativar_itens_cardapio_unidade_converte_ids_e_ignora_invalidos():
    service = EditarItensCardapioService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = [{"id": 10}, {"id": 20}]

    with patch("src.services.editar_itens_cardapio_service.requests.post", return_value=fake_resp) as mock_post:
        resultado = service.ativar_itens_cardapio_unidade([10, "20", "a", None])

    # payload enviado deve conter apenas inteiros válidos
    called_json = mock_post.call_args.kwargs["json"]
    assert called_json == {"itens": [10, 20]}
    assert isinstance(called_json["itens"][0], int)
    assert isinstance(called_json["itens"][1], int)

    assert isinstance(resultado, list)
    assert len(resultado) == 2
    assert resultado[0]["id"] == 10


def test_ativar_itens_cardapio_unidade_retorna_lista_vazia_quando_json_nao_e_lista():
    service = EditarItensCardapioService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = {"status": "ok"}

    with patch("src.services.editar_itens_cardapio_service.requests.post", return_value=fake_resp):
        resultado = service.ativar_itens_cardapio_unidade([1, 2, 3])

    assert resultado == []


def test_ativar_itens_cardapio_unidade_propaga_http_error():
    service = EditarItensCardapioService()

    fake_resp = Mock()
    fake_resp.raise_for_status.side_effect = requests.HTTPError("Erro 400")
    fake_resp.json.return_value = []

    with patch("src.services.editar_itens_cardapio_service.requests.post", return_value=fake_resp):
        with pytest.raises(requests.HTTPError):
            service.ativar_itens_cardapio_unidade([1, 2])


# ---------- remover_itens_cardapio_unidade ----------

def test_remover_itens_cardapio_unidade_ids_vazio_lanca_valueerror():
    service = EditarItensCardapioService()

    with pytest.raises(ValueError, match="A lista de IDs não pode ser vazia"):
        service.remover_itens_cardapio_unidade([])


def test_remover_itens_cardapio_unidade_todos_ids_invalidos_lanca_valueerror():
    service = EditarItensCardapioService()

    with pytest.raises(ValueError, match="Nenhum ID válido foi informado"):
        service.remover_itens_cardapio_unidade(["x", None, "y"])


def test_remover_itens_cardapio_unidade_converte_ids_e_ignora_invalidos():
    service = EditarItensCardapioService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = [{"id": 10}, {"id": 30}]

    with patch("src.services.editar_itens_cardapio_service.requests.delete", return_value=fake_resp) as mock_delete:
        resultado = service.remover_itens_cardapio_unidade([10, "30", "a"])

    called_json = mock_delete.call_args.kwargs["json"]
    assert called_json == {"itens": [10, 30]}

    assert isinstance(resultado, list)
    assert len(resultado) == 2
    assert resultado[1]["id"] == 30


def test_remover_itens_cardapio_unidade_propaga_http_error():
    service = EditarItensCardapioService()

    fake_resp = Mock()
    fake_resp.raise_for_status.side_effect = requests.HTTPError("Erro 500")
    fake_resp.json.return_value = []

    with patch("src.services.editar_itens_cardapio_service.requests.delete", return_value=fake_resp):
        with pytest.raises(requests.HTTPError):
            service.remover_itens_cardapio_unidade([1, 2])


# ---------- listar_cardapio_central ----------

def test_listar_cardapio_central_retorna_lista_quando_json_e_lista():
    service = EditarItensCardapioService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = [
        {"id": 10, "COMIDA": "X-Salada"},
        {"id": 20, "COMIDA": "X-Burger"},
    ]

    with patch("src.services.editar_itens_cardapio_service.requests.get", return_value=fake_resp) as mock_get:
        resultado = service.listar_cardapio_central()

    mock_get.assert_called_once_with("http://127.0.0.1:8000/cardapio/central")
    assert isinstance(resultado, list)
    assert len(resultado) == 2
    assert resultado[1]["COMIDA"] == "X-Burger"


def test_listar_cardapio_central_retorna_lista_vazia_quando_json_nao_e_lista():
    service = EditarItensCardapioService()

    fake_resp = Mock()
    fake_resp.raise_for_status.return_value = None
    fake_resp.json.return_value = {"erro": "formato inválido"}

    with patch("src.services.editar_itens_cardapio_service.requests.get", return_value=fake_resp):
        resultado = service.listar_cardapio_central()

    assert resultado == []