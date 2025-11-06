from src.services.pedidos_fila_service import PedidosFilaService
from datetime import datetime

class VisualizarPedidosFilaController:
    def __init__(self, services: PedidosFilaService):
        self.services = services

    def consultar(self):
        return self.services.listar_pedidos_ativos()
    


    @staticmethod
    def horario_formatado(v):
        try:
            ts = int(str(v).strip())
            # se vier em milissegundos (13 dígitos), converte para segundos
            if ts > 10**12:
                ts = ts // 1000
            return datetime.fromtimestamp(ts).strftime("%d/%m/%Y %H:%M:%S")
        except Exception:
            return str(v)