while True:
    print("\n" + "┌" + "─"*44 + "┐")
    print("│{:^44}│".format("BEM-VINDO AO BURGUER FEI"))
    print("├" + "─"*44 + "┤")
    print("│  1) Realizar pedido                        │")
    print("│  2) Visualizar pedidos na fila             │")
    print("│  3) Editar itens no cardápio               │")
    print("│  4) Visualizar cardápio                    │")
    print("│  5) Sair                                   │")
    print("└" + "─"*44 + "┘\n")


    try:
        option = int(input("Escolha uma opção [1-5]: "))

        if option not in range(1,6):
            print("ERRO Digite uma opção [1-5]")
            continue

        match option:
            case 1:
                print("---- Entrou no 1 ----")
            case 2:
                print("---- Entrou no 2 ----")
            case 3:
                print("---- Entrou no 3 ----")
            case 4:
                print("---- Entrou no 4 ----")
            case 5:
                exit()

    except ValueError:
        print("ERRO Digte um número válido")  # digitou letra, vazio, 3.5, etc.
        continue

        
    

        
    
