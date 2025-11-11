from types import SimpleNamespace
from codigo.services.pedidos_fila_service import PedidosFilaService

service = PedidosFilaService()

def fake_get_pedidos_ativos(url, timeout=10):
    return SimpleNamespace(
        raise_for_status=lambda: None,
        json=lambda: [
            {
                "NUMERO_PEDIDO": "1001",
                "NOME_CLIENTE": "João Silva",
            }
        ],
    )

def test_listar_pedidos_ativos(monkeypatch):
    monkeypatch.setattr(
        "src.services.pedidos_fila_service.requests.get",
        fake_get_pedidos_ativos,
    )


    resultado = service.listar_pedidos_ativos()

    assert resultado == [
        {
            "NUMERO_PEDIDO": "1001",
            "NOME_CLIENTE": "João Silva",
        }
    ]