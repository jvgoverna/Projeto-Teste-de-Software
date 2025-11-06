from src.services.visualizar_cardapio_service import VisualizarCardapioService
class VisualizarCardapioController:
    def __init__(self, service: VisualizarCardapioService):
        self.service = service

    def view_menu(self):
        return self.service.view_menu()
