from types import SimpleNamespace

from codigo.services.visualizar_notas_fiscais_service import VisualizarNotasFiscaisService

service = VisualizarNotasFiscaisService()

def fake_visualizar_notas_fiscais(url, timeout=10):
    return SimpleNamespace(
        raise_for_status=lambda: None,
        json=lambda: [
            {
                "id": 3,
                "NUMERO_PEDIDO":"1001",
                "NOME_CLIENTE":"João Silva",
                "CPF":"123456789",
                "PRECO": "1500"
            },
        ],
    )

def fake_visualizar_notas_fiscais_preco_invalido(url, timeout=10):
    return SimpleNamespace(
        raise_for_status=lambda: None,
        json=lambda: [
            {
                "id": 3,
                "NUMERO_PEDIDO":"1001",
                "NOME_CLIENTE":"João Silva",
                "CPF":"123456789",
                "PRECO": "aa"
            },
        ],
    )

def test_visualizar_notas_fiscais(monkeypatch):

    monkeypatch.setattr(
        "src.services.visualizar_notas_fiscais_service.requests.get",
        fake_visualizar_notas_fiscais,
    )

    resultado = service.listar_notas_fiscais()

    assert resultado == [
        {"NUMERO_PEDIDO": "1001", "NOME_CLIENTE": "João Silva", "CPF": "123456789", "PRECO":15.0},
    ]


def test_visualizar_notas_fiscais(monkeypatch):

    monkeypatch.setattr(
        "src.services.visualizar_notas_fiscais_service.requests.get",
        fake_visualizar_notas_fiscais_preco_invalido,
    )

    resultado = service.listar_notas_fiscais()

    assert resultado == [
        {"NUMERO_PEDIDO": "1001", "NOME_CLIENTE": "João Silva", "CPF": "123456789", "PRECO": 0.0},
    ]