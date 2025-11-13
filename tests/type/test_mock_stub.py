# tests/type/test_mock_stub.py

import pytest
from unittest.mock import Mock
from fastapi.testclient import TestClient

from Server.BurgerFeiAPI import app, get_db


# =========================
# Fixtures
# =========================

@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def db_mock():
    return Mock()


@pytest.fixture(autouse=True)
def override_db_dependency(db_mock):
    """
    Override global da dependency get_db para usar o mock
    em todos os testes deste arquivo.
    """
    app.dependency_overrides[get_db] = lambda: db_mock
    yield
    app.dependency_overrides.clear()


# =========================
# /db/ping com mock de DB
# =========================

def test_ping_db_sucesso_com_mock(client, db_mock):
    conn_mock = Mock()
    cursor_mock = Mock()
    cursor_mock.fetchone.return_value = (1,)
    conn_mock.execute.return_value = cursor_mock

    db_mock.conexao_ativa_banco_sqlite = conn_mock
    db_mock.caminho_completo_arquivo_banco_sqlite = "mocked.db"

    resp = client.get("/db/ping")

    assert resp.status_code == 200
    data = resp.json()
    assert data["db"] == "connected"
    assert data["path"] == "mocked.db"
    conn_mock.execute.assert_called_once()


def test_ping_db_erro_quando_execute_lanca_excecao(client, db_mock):
    conn_mock = Mock()
    conn_mock.execute.side_effect = Exception("Falha no SELECT 1")

    db_mock.conexao_ativa_banco_sqlite = conn_mock

    resp = client.get("/db/ping")

    assert resp.status_code == 500
    data = resp.json()
    assert "Falha ao consultar o banco" in data["detail"]


# =========================
# /cardapio/unidade com mock
# =========================

def test_listar_cardapio_unidade_usa_valor_do_db(client, db_mock):
    db_mock.ler_todos_os_registros_da_tabela.return_value = [
        {"id": 1, "COMIDA": "X-SALADA", "PRECO": "2000", "TEMPO_PREPARO": "8"},
        {"id": 2, "COMIDA": "X-BURGUER", "PRECO": "1700", "TEMPO_PREPARO": "7"},
    ]

    resp = client.get("/cardapio/unidade")

    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 2
    assert data[0]["COMIDA"] == "X-SALADA"
    db_mock.ler_todos_os_registros_da_tabela.assert_called_once_with("CARDAPIO_UNIDADE")


def test_listar_cardapio_unidade_quando_db_lanca_excecao(client, db_mock):
    db_mock.ler_todos_os_registros_da_tabela.side_effect = Exception("Erro lendo tabela")

    resp = client.get("/cardapio/unidade")

    assert resp.status_code == 500
    data = resp.json()
    assert "Erro ao consultar CARDAPIO_UNIDADE" in data["detail"]


# =========================
# /cardapio/unidade/itens (DELETE) com mock
# =========================

def test_remover_itens_unidade_sucesso_com_mock(client, db_mock):
    """
    Simula remoção bem-sucedida para dois IDs.
    Como não configuramos side_effect, o Mock não levanta exceção.
    """
    resp = client.request(
        "DELETE",
        "/cardapio/unidade/itens",
        json={"itens": [1, 2]},
    )

    assert resp.status_code == 200
    data = resp.json()

    assert data["quantidade_de_itens_removidos"] == 2
    assert isinstance(data["lista_de_erros_durante_remocao"], list)
    assert data["lista_de_erros_durante_remocao"] == []

    # chamada precisa ter sido feita 2x (para id=1 e id=2)
    assert db_mock.remover_registro_da_tabela_por_id.call_count == 2


def test_remover_itens_unidade_quando_db_falha_em_um_id(client, db_mock):
    """
    Simula falha só no ID 2. O endpoint deve:
    - contar 1 removido com sucesso
    - registrar um erro na lista de erros
    """

    def side_effect(nome_da_tabela, valor_id_do_registro_para_remover):
        if valor_id_do_registro_para_remover == 2:
            raise Exception("Erro ao remover id 2")

    db_mock.remover_registro_da_tabela_por_id.side_effect = side_effect

    resp = client.request(
        "DELETE",
        "/cardapio/unidade/itens",
        json={"itens": [1, 2]},
    )

    assert resp.status_code == 200
    data = resp.json()

    assert data["quantidade_de_itens_removidos"] == 1
    assert len(data["lista_de_erros_durante_remocao"]) == 1
    assert data["lista_de_erros_durante_remocao"][0]["id"] == "2"
    assert "Erro ao remover" in data["lista_de_erros_durante_remocao"][0]["erro"]