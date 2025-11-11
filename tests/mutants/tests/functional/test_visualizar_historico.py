from types import SimpleNamespace 
from codigo.services.visualizar_historico_service import HistoricoService

service = HistoricoService()

def fake_listar_historico(url,timeout=10):
    return SimpleNamespace(
        raise_for_status=lambda: None,
        json=lambda: [
            {
                "id": 3,
                "NUMERO_PEDIDO":"1001",
                "NOME_CLIENTE":"João Silva",
                "CPF":"123456789",
                "COMIDAS": "BATATA FRITA",
                "PRECO": "1700",
                "TEMPO_PREPARO": "6",
                "HORARIO_ADICIONADO": "1730471500"
            },
        ],
    )


def test_listar_historico(monkeypatch):

    monkeypatch.setattr(
        "src.services.visualizar_historico_service.requests.get",
        fake_listar_historico,
    )

    resultado = service.listar_historico()

    assert resultado == [
        {"id": 3,"NUMERO_PEDIDO": "1001", "NOME_CLIENTE": "João Silva", "CPF": "123456789", "COMIDAS": 
        "BATATA FRITA", "PRECO" : "1700", "TEMPO_PREPARO" : "6", "HORARIO_ADICIONADO" : "1730471500"},
    ]