from src.controllers.visualizar_pedidos_fila_controller import VisualizarPedidosFilaController
from src.services.pedidos_fila_service import PedidosFilaService

def main():
    try:
        visualizar_ctrl = VisualizarPedidosFilaController(PedidosFilaService())

        pedidos = visualizar_ctrl.consultar()

        if not pedidos:
            print("Não há pedidos em preparo.")
            return
        else:
            print(pedidos)
            for i in pedidos:

                horario = visualizar_ctrl.horario_formatado(i.get("HORARIO_ADICIONADO"))

                print("\n" + "┌" + "─"*44 + "┐")
                print(f"│{('PEDIDO NÚMERO ' + str(i.get('id'))):<44}│")
                print("├" + "─"*44 + "┤")
                print(f"│  CLIENTE: {i.get('NOME_CLIENTE'):<33}│")
                print(f"│  CPF: {i.get('CPF'):<37}│")
                print(f"│  COMIDAS: {i.get('COMIDAS')}│")
                print(f"│  PREÇO: {i.get('PRECO'):<35}│")
                print(f"│  TEMPO DE PREPRARO: {i.get('TEMPO_PREPARO')}│")
                print("│" + f"{'  HORÁRIO DO PEDIDO: ' + horario:<44}" + "│")
                print("├" + "─"*44 + "┤")
    except Exception as e:
        print("❌ Erro ao consultar pedidos ativos:")
        print(e)

if __name__ == "__main__":
    main()