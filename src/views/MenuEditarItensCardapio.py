from src.services.editar_itens_cardapio_service import EditarItensCardapioService
from src.controllers.editar_itens_cardapio_controller import EditarItensCardapioController
from src.utils.formatting import imprimir_titulo, imprimir_linhas_cardapio_central, imprimir_rodape

def main():
    try:
        editar_ctrl = EditarItensCardapioController(EditarItensCardapioService())

        itens_unidade = editar_ctrl.mostrar_cardapio_unidade()
        itens_cardapio = editar_ctrl.mostrar_cardapio_central()

        if not itens_unidade:
            # Não há itens na unidade -> mostrar Central e permitir adicionar
            print("Nenhum item ativo no cardápio da unidade")
            imprimir_titulo("CARDÁPIO CENTRAL")
            imprimir_linhas_cardapio_central(itens_cardapio)
            imprimir_rodape()

            # Selecionar para adicionar (um número por vez, na controller)
            editar_ctrl.selecionar_itens_para_adicionar_por_indice()

        else:
            # Há itens na unidade -> mostrar Unidade
            imprimir_titulo("CARDÁPIO UNIDADE")
            imprimir_linhas_cardapio_central(itens_unidade)
            imprimir_rodape()

            # Perguntar se quer adicionar mais itens
            resposta = input("Deseja adicionar mais algum item no cardápio? (s/n): ").strip().lower()
            if resposta == "s":
                imprimir_titulo("CARDÁPIO CENTRAL")
                imprimir_linhas_cardapio_central(itens_cardapio)
                imprimir_rodape()
                editar_ctrl.selecionar_itens_para_adicionar_por_indice()

        # Após possível adição, oferecer remover itens
        remover = input("Deseja remover algum item no cardápio? (s/n): ").strip().lower()
        if remover == "s":
            editar_ctrl.selecionar_itens_para_remover_por_indice()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
