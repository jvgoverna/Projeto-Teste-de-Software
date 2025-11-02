from src.views import MenuRealizarPedido
from src.views import MenuVisualizarCardapio


while True:
    print("\n" + "┌" + "─"*44 + "┐")
    print("│{:^44}│".format("BEM-VINDO AO BURGUER FEI"))
    print("├" + "─"*44 + "┤")
    print("│  1) Realizar pedido                        │") # PEDIDO
    print("│  2) Visualizar pedidos na fila             │") # MOSTRAR PEDIDOS ATIVOS
    print("│  3) Editar itens no cardápio               │") # METODOS DO CARDAPIO
    print("│  4) Visualizar cardápio                    │") # VER CARDAPIO
    print("│  5) Notas fiscais                          │") # ver notas fiscais
    print("│  6) Ver historico de pedidos               │") #Historico de pedidos
    print("│  7) Sair                                   │") # Fechar conexao
    print("└" + "─"*44 + "┘\n")

    try:
        option = int(input("Escolha uma opção [1-5]: "))

        if option not in range(1,8):
            print("ERRO Digite uma opção [1-5]")
            continue

        match option:
            case 1:
                print("---- Entrou no 1 ----")
                MenuRealizarPedido.main()
            case 2:
                print("---- Entrou no 2 ----")
            case 3:
                print("---- Entrou no 3 ----")
            case 4:
                print("---- Entrou no 4 ----")
                MenuVisualizarCardapio.main()
            case 5:
                exit()

    except ValueError:
        print("ERRO Digte um número válido")
        continue