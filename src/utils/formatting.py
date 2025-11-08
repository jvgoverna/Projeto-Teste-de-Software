LARGURA = 52

def imprimir_titulo(txt: str):
    print("┌" + "─" * LARGURA + "┐")
    print("│{:^{w}}│".format(txt, w=LARGURA))
    print("├" + "─" * LARGURA + "┤")

def imprimir_linhas(itens):
    # Reservas: "NN) " = 4 colunas; " R$ " = 4; preço = 6; "   " = 3; "({tempo} min)" ~ 8
    # Antes, o nome tinha 30; com índice, reduzimos para 26 para manter o total.
    nome_width = 26
    for idx, item in enumerate(itens, 1):
        nome = item["nome"]
        preco = item["preco"]
        tempo = item["tempo_preparo"]

        linha = f"{idx:>2}) {nome:<{nome_width}} R$ {preco:>6.2f}   ({tempo} min)"
        # Garante que a área interna tenha exatamente LARGURA caracteres
        print("│ " + f"{linha:<{LARGURA-2}}"[:LARGURA-2] + "│")

def imprimir_linhas_cardapio_central(itens):
    nome_width = 26
    for idx, item in enumerate(itens, 1):
        nome = item["COMIDA"]

        try:
            preco = int(item["PRECO"]) / 100
        except (TypeError, ValueError):
            preco = 0.0
        
        tempo = item["TEMPO_PREPARO"]

        linha = f"{idx:>2}) {nome:<{nome_width}} R$ {preco:>6.2f}   ({tempo} min)"
        # Garante que a área interna tenha exatamente LARGURA caracteres
        print("│ " + f"{linha:<{LARGURA-2}}"[:LARGURA-2] + "│")


def imprimir_rodape():
    print("└" + "─" * LARGURA + "┘\n")