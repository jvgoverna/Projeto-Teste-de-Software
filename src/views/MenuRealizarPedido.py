from src.controllers.realizar_pedido_controller import RealizarPedidoController
from src.controllers.visualizar_cardapio_controller import VisualizarCardapioController
from src.services.realizar_pedido_service import RealizarPedidoService
from src.controllers.visualizar_cardapio_controller import VisualizarCardapioService

def main():
    
    visualizarCardapio = VisualizarCardapioController(VisualizarCardapioService())

    visualizarCardapio.view_menu()

    try:
        order = []
        choose = int(input("Digite uma opção: "))

        last_key = next(reversed(VisualizarCardapioService.products), None)

        #print("Última chave: ",last_key)

        if choose not in range(1,int(last_key) + 1):
            print("ERRO ao adicionar pedido")
        else:
            units = int(input("Digite o número de unidades: "))

            for product in VisualizarCardapioService.products:
                if str(choose) == product:
                    order.append(VisualizarCardapioService.products[str(choose)]["Titulo"])

            print(order)        
        
    except ValueError:
        print("ERRO Digite um número válido, pedido cancelado")



if __name__ == "__main__":
    main()