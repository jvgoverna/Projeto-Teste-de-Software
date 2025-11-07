from src.services.visualizar_notas_fiscais_service import VisualizarNotasFiscaisService

from datetime import datetime

class VisualizarNotasFiscaisController:

    def __init__(self, service: VisualizarNotasFiscaisService):
        self.service = service

    def consultar(self):
        return self.service.listar_notas_fiscais()

    @staticmethod
    def data_formatada(v):
        try:
            ts = int(str(v).strip())
            # se vier em milissegundos (13 dígitos), converte para segundos
            if ts > 10**12:
                ts = ts // 1000
            return datetime.fromtimestamp(ts).strftime("%d/%m/%Y %H:%M:%S")
        except Exception:
            return str(v)