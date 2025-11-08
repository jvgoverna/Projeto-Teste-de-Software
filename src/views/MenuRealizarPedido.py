from src.controllers.visualizar_cardapio_controller import VisualizarCardapioController
from src.services.visualizar_cardapio_service import VisualizarCardapioService
from src.controllers.realizar_pedido_controller import RealizarPedidoController
from src.services.realizar_pedido_service import RealizarPedidoService
from itertools import count

from src.utils.formatting import imprimir_titulo, imprimir_linhas, imprimir_rodape

def montar_indices_menu(itens):
    """
    Retorna:
      - precos[nome] -> preco_em_reais (float)
      - tempos[nome] -> tempo_em_minutos (int ou 0)
      - idx_to_nome[i] -> nome do item (1-based)
    """
    precos = {}
    tempos = {}
    idx_to_nome = {}
    for i, it in enumerate(itens, 1):
        nome = str(it["nome"]).strip()
        precos[nome] = float(it["preco"])
        try:
            tempos[nome] = int(it["tempo_preparo"])
        except Exception:
            tempos[nome] = 0
        idx_to_nome[i] = nome
    return precos, tempos, idx_to_nome

# contador 1-based em memória
_pedido_counter = count(1)

def main():
    # 1) Mostrar cardápio
    cardapio_ctrl = VisualizarCardapioController(VisualizarCardapioService())
    itens = cardapio_ctrl.view_menu()

    if not itens:
        print("⚠️ Nenhum produto encontrado no cardápio.")
        return

    imprimir_titulo("CARDÁPIO DA UNIDADE")
    imprimir_linhas(itens)  # já numerado (1,2,3…)
    imprimir_rodape()

    # 2) Índices e dicionários para cálculo
    precos, tempos, idx_to_nome = montar_indices_menu(itens)

    # 3) Coletar dados do pedido
    print("Preencha os dados para realizar o pedido:")
    nome_cliente = input("Nome do cliente: ").strip()
    cpf = input("CPF: ").strip()


    realizar_ctrl = RealizarPedidoController(RealizarPedidoService())
    print("\nSelecione os itens pelo NÚMERO mostrado no cardápio.")
    comidas = realizar_ctrl.selecionar_itens_por_indice(idx_to_nome)

    if not comidas:
        print("❌ Nenhum item informado.")
        return

    # 4) Calcular preço total e tempo total
    preco_total = 0.0
    tempo_total_min = 0
    for nome in comidas:
        preco_total += precos.get(nome, 0.0)
        tempo_total_min += tempos.get(nome, 0)

    if preco_total <= 0:
        print("❌ Não foi possível calcular o preço total. Verifique os itens.")
        return

    # 5) Enviar para a API
    try:
        resultado = realizar_ctrl.realizar_pedido(
            numero_pedido=next(_pedido_counter),  # usa o próximo id
            nome_cliente=nome_cliente,
            cpf=cpf,
            comidas=comidas,
            preco_total_reais=preco_total,
            tempo_preparo_total_min=tempo_total_min,
        )
        print("\n✅ Pedido criado com sucesso!")
        print(f"Mensagem: {resultado.get('mensagem', '(sem mensagem)')}")
        print(f"ID pedido inserido: {resultado.get('id_pedido_inserido')}")
        print(f"ID nota fiscal inserida: {resultado.get('id_nota_fiscal_inserida')}")

        # --- ATUALIZAR STATUS DOS PEDIDOS APÓS CRIAR ---
        try:
            resumo = realizar_ctrl.atualizar_status_pedidos()
            print("\n🔄 Status de pedidos atualizado.")

            movidos_qtd = resumo.get("quantidade_movidos_para_historico", 0)
            movidos_ids = resumo.get("ids_movidos_para_historico", [])
            erros = resumo.get("erros", [])
            ainda = resumo.get("resumo_ainda_ativos", [])

            print(f" - Movidos para histórico: {movidos_qtd} (ids: {', '.join(map(str, movidos_ids)) or '—'})")
            if erros:
                print(" - Erros durante a atualização:")
                for e in erros:
                    print(f"    id={e.get('id')} -> {e.get('erro')}")
            if ainda:
                print(" - Ainda ativos (faltam segundos):")
                for r in ainda:
                    print(f"    id={r.get('id')} NUMERO_PEDIDO={r.get('NUMERO_PEDIDO')} faltam={r.get('faltam_segundos')}s")
        except Exception as e:
            print("⚠️ Não foi possível atualizar o status dos pedidos agora:")
            print(e)
        
    except Exception as e:
        print("❌ Erro ao criar pedido:")
        print(e)

if __name__ == "__main__":
    main()