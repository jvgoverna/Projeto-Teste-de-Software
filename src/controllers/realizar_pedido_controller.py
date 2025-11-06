from src.services.realizar_pedido_service import RealizarPedidoService

class RealizarPedidoController:
    def __init__(self, service: RealizarPedidoService):
        self.service = service

    def realizar_pedido(self,
        numero_pedido: str,
        nome_cliente: str,
        cpf: str,comidas: list[str],
        preco_total_reais: float,
        tempo_preparo_total_min: int,
    ):
        return self.service.criar_pedido(
            numero_pedido=numero_pedido,
            nome_cliente=nome_cliente,
            cpf=cpf,
            comidas=comidas,
            preco_total_reais=preco_total_reais,
            tempo_preparo_total_min=tempo_preparo_total_min,
        )
    
    def selecionar_itens_por_indice(self, idx_to_nome: dict) -> list[str]:
        """
        Pergunta um índice por vez. Cada confirmação adiciona 1 unidade.
        Sai quando a resposta não for 's' (default N).
        """

        comidas = []
        total = len(idx_to_nome)

        try:
            while True:
                s = input(f"Digite o NÚMERO do item [1-{total}]: ").strip()
                try:
                    i = int(s)
                    if not (1 <= i <= total):
                        print("⚠️ Número fora do cardápio. Tente novamente.")
                        continue
                except Exception:
                    print("⚠️ Digite apenas números válidos.")
                    continue

                nome = idx_to_nome[i]
                comidas.append(nome)
                print(f"➕ Adicionado: {nome}")

                mais = input("Deseja adicionar mais algum? (s/N): ").strip().lower()
                if mais != "s":
                    break
        except (KeyboardInterrupt, EOFError):
            print("\n Entrada interrompida. Finalizando seleção com os itens já adicionados.")

        return comidas
