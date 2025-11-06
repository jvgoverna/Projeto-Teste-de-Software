from src.controllers.visualizar_cardapio_controller import VisualizarCardapioController
from src.services.visualizar_cardapio_service import VisualizarCardapioService
from src.utils.formatting import imprimir_titulo, imprimir_linhas, imprimir_rodape

def main():
    controller = VisualizarCardapioController(VisualizarCardapioService())
    try:
        itens = controller.view_menu()

        if not itens:
            print("⚠️ Nenhum produto encontrado no cardápio.")
            return

        imprimir_titulo("CARDÁPIO DA UNIDADE")
        imprimir_linhas(itens)
        imprimir_rodape()
    except Exception as e:
        print("❌ Erro ao obter cardápio:")
        print(e)

if __name__ == "__main__":
    main()