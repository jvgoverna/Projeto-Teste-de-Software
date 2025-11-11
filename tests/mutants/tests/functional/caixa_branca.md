# Comando para rodar os testes funcionais de Caixa Branca:

PYTHONPATH=. pytest "tests/functional" \
  --cov=src.services.realizar_pedido_service \
  --cov=src.services.pedidos_fila_service \
  --cov=src.services.editar_itens_cardapio_service\
  --cov=src.services.visualizar_cardapio_service\
  --cov=src.services.visualizar_notas_fiscais_service\
  --cov=src.services.visualizar_historico_service\
  --cov-branch \
  --cov-report=html && xdg-open htmlcov/index.html

## Obs.: Precisa rodar com o banco de dados ativo