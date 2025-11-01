from src.controllers.visualizar_cardapio_controller import VisualizarCardapioController
from src.services.visualizar_cardapio_service import VisualizarCardapioService

def main():
    controller = VisualizarCardapioController(VisualizarCardapioService())
    controller.view_menu()

if __name__ == "main":
    main()