from src.services.realizar_pedido_service import RealizarPedidoService

class RealizarPedidoController:
    def __init__(self, service: RealizarPedidoService):
        self.service = service

    
