from src.services.editar_itens_cardapio_service import EditarItensCardapioService

class EditarItensCardapioController:

    def __init__(self, service: EditarItensCardapioService):
        self.service = service

    def mostrar_cardapio_unidade(self):
        return self.service.listar_cardapio_unidade()
    
    def ativar_itens_cardapio_unidade(self, ids: list[int]) -> dict:
        print(f"Itens adicionados: {ids}")
        return self.service.ativar_itens_cardapio_unidade(ids)

    def remover_itens_cardapio_unidade(self, ids: list[int]) -> dict:
        print("Itens removidos")
        return self.service.remover_itens_cardapio_unidade(ids)

    def selecionar_itens_para_adicionar_por_indice(self):
        numeros = []
        while True:
            num = input("Digite o NÚMERO do item que deseja ativar: ").strip()
            try:
                indices = int(num)
                if indices not in numeros:
                    numeros.append(indices)

                if not (1 <= indices <= 12):
                    print("⚠️ Número fora do cardápio. Tente novamente.")
                    continue

            except Exception:
                print("⚠️ Digite apenas números válidos.")
                continue

            mais = input("Deseja adicionar mais algum? (s/N): ").strip().lower()

            if mais != "s":
                break
        
        self.ativar_itens_cardapio_unidade(numeros)

    def selecionar_itens_para_remover_por_indice(self):
        # pega a lista atual exibida para saber o tamanho e mapear índice -> id
        itens_unidade = self.mostrar_cardapio_unidade()
        total = len(itens_unidade)

        numeros = []
        while True:
            num = input("Digite o NÚMERO do item que deseja remover: ").strip()

            if not num.isdigit():
                print("⚠️ Digite apenas números válidos.")
                continue

            indices = int(num)

            # valida pelo tamanho real da lista
            if not (1 <= indices <= total):
                print(f"⚠️ Número fora do cardápio (válidos: 1..{total}). Tente novamente.")
                continue

            # evita duplicados
            if indices in numeros:
                print(f"⚠️ O número {indices} já foi selecionado. Ignorado.")
            else:
                numeros.append(indices)

            mais = input("Deseja remover mais algum? (s/N): ").strip().lower()
            if mais != "s":
                break

        # converte índices escolhidos para IDs reais
        ids_para_remover = []
        for idx in numeros:
            item = itens_unidade[idx - 1]  # índice 1-based na tela -> 0-based na lista
            try:
                ids_para_remover.append(int(item.get("id")))
            except (TypeError, ValueError):
                pass  # ignora itens sem id válido

        if not ids_para_remover:
            print("⚠️ Nenhum item válido selecionado para remoção.")
            return

        # chama a operação de remoção com IDs
        self.remover_itens_cardapio_unidade(ids_para_remover)

    def mostrar_cardapio_central(self):
        return self.service.listar_cardapio_central()