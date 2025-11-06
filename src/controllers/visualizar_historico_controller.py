from src.services.visualizar_historico_service import HistoricoService
from datetime import datetime

class VisualizarHistoricoController:

    def __init__(self, service: HistoricoService):
        self.service = service

    def consultar(self):
        return self.service.listar_historico()

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