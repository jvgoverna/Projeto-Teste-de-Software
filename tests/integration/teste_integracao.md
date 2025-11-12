# Testes de Integração – Sistema de Pedidos

Este documento descreve o conjunto de testes de integração implementados para o sistema de pedidos do restaurante (módulos de cardápio, fila de preparo, histórico e notas fiscais).

# Objetivo dos testes

Os testes de integração têm como objetivo verificar se:

Os módulos de serviço (RealizarPedidoService, PedidosFilaService, HistoricoService, VisualizarNotasFiscaisService, EditarItensCardapioService) funcionam corretamente em conjunto.

A integração com o banco de dados está coerente (criação, consulta e atualização de registros).

Os fluxos completos de negócio (criar pedido, colocar na fila, finalizar, enviar para histórico, etc.) se comportam conforme as regras definidas.

# Resultado da execução dos testes de integração

✅ **8 testes passaram**  
- Validam fluxos completos como criação de pedido válido, inclusão na fila de preparo, registro no histórico e geração de notas fiscais, garantindo que os serviços se comunicam corretamente entre si e com o banco de dados.

---

❌ **2 testes falharam (bugs de regra de negócio identificados)**  

- **`test_criar_pedido_com_numero_pedido_duplicado`**  
  - Verifica se o sistema impede a criação de dois pedidos com o **mesmo `NUMERO_PEDIDO`**.  
  - Resultado atual: o mesmo número está sendo aceito mais de uma vez, indicando que **não existe validação de unicidade** para o número do pedido.

- **`test_criar_pedido_com_comidas_vazias`**  
  - Verifica se o sistema **rejeita pedidos cuja lista de `COMIDAS` está vazia**.  
  - Resultado atual: o sistema permite criar e persistir um pedido sem itens de comida, o que **violaria a regra de negócio** (não faz sentido ter um pedido sem produtos).

> Esses dois testes foram mantidos propositalmente como falhando para evidenciar problemas que ainda precisam ser corrigidos na implementação. Depois de ajustar as validações, a expectativa é que todos os testes fiquem: **✅ 10 passed, 0 failed**.

# Comando para rodar os testes de integração

PYTHONPATH=. pytest "tests/integration"

## Obs.: é obrigatório estar com o banco de dados e a API ativos

### Passo a passo para subir a API antes de rodar os testes

1. Abra um terminal na sua máquina.
2. Vá até a pasta `src` do projeto: `cd ~/Documentos/GitHub/Projeto-Teste-de-Software/src`
3. Rode o comando: `uvicorn Server.BurgerFeiAPI:app --reload --port 8000`
