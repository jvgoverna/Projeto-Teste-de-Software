from src.services.visualizar_notas_fiscais_service import VisualizarNotasFiscaisService
from src.controllers.visualizar_notas_fiscais_controller import VisualizarNotasFiscaisController

# Resposta (200): [ { "id": 1, "NUMERO_PEDIDO": "1001", "NOME_CLIENTE": "João Silva", "CPF": "11122233344", "PRECO": "2100" }, { "id": 2, "NUMERO_PEDIDO": "1002", "NOME_CLIENTE": "Maria Oliveira", "CPF": "99988877766", "PRECO": "1700" } ]

def main():
    try:
        visualizar_notas_ctrl = VisualizarNotasFiscaisController(VisualizarNotasFiscaisService())

        notas_fiscais = visualizar_notas_ctrl.consultar()

        if not notas_fiscais:
            print("Não há notas fiscais disponíveis.")
            return
        else:          
            for nota in notas_fiscais:
                print("\n" + "┌" + "─"*44 + "┐")
                print(f"│{('NOTA FISCAL PEDIDO NÚMERO ' + str(nota.get('NUMERO_PEDIDO'))):<44}│")
                print("├" + "─"*44 + "┤")
                print(f"│  CLIENTE: {nota.get('NOME_CLIENTE'):<33}│")
                print(f"│  CPF: {nota.get('CPF'):<37}│")
                print(f"│  PREÇO: R$ {nota.get('PRECO'):<33.2f}│")
                print("├" + "─"*44 + "┤")
    except Exception as e:
        print("❌ Erro ao consultar notas fiscais:")
        print(e)

if __name__ == "__main__":
    main()  
