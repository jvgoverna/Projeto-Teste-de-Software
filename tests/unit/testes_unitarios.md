# Testes Unitários – Burguer FEI

| **ID** | **Título / Objetivo do Teste** | **Regra / Comportamento Validado** | **Pré-condição** | **Entradas / Operações** | **Resultado Esperado** |
|--------|--------------------------------|------------------------------------|------------------|---------------------------|-------------------------|
| **TU01** | Validar retorno normal do cardápio da unidade | Serviço deve retornar lista válida de itens | Resposta HTTP 200 simulada | Chamada `EditarItensCardapioService.listar_cardapio_unidade()` com `requests.get` mockado retornando lista de itens | Retorna uma lista com itens contendo campos esperados (ex.: `COMIDA == "X-Salada"`). |
| **TU02** | Cardápio da unidade com JSON em formato inválido | Em caso de JSON não-lista, retornar lista vazia | Resposta JSON simulada como dict | Chamada `listar_cardapio_unidade()` com `json()` retornando `{"erro": "formato inválido"}` | Retorna `[]`. |
| **TU03** | Propagação de erro HTTP ao listar cardápio da unidade | Erros HTTP não devem ser engolidos | `raise_for_status` lança `requests.HTTPError` | Chamada `listar_cardapio_unidade()` com `raise_for_status` mockado lançando erro | Lança `requests.HTTPError`. |
| **TU04** | Validação de lista de IDs vazia ao ativar itens | Não deve aceitar lista de IDs vazia | Lista de IDs vazia | Chamada `ativar_itens_cardapio_unidade([])` | Lança `ValueError` com mensagem sobre lista de IDs vazia. |
| **TU05** | Validação de IDs totalmente inválidos ao ativar itens | Nenhum ID válido ⇒ erro de validação | Lista contendo apenas valores inválidos | Chamada `ativar_itens_cardapio_unidade(["a", None, "xyz"])` | Lança `ValueError` indicando ausência de IDs válidos. |
| **TU06** | Conversão e limpeza de IDs ao ativar itens | Somente inteiros válidos devem ser enviados ao backend | Resposta HTTP 200 simulada | Chamada `ativar_itens_cardapio_unidade([10, "20", "a", None])` com `requests.post` mockado | JSON enviado é `{"itens": [10, 20]}` (apenas inteiros válidos) e retorno é uma lista com itens (`id` 10 e 20). |
| **TU07** | Resposta inválida ao ativar itens | JSON não-lista deve ser tratado como vazio | Backend retorna dict | Chamada `ativar_itens_cardapio_unidade([1, 2, 3])` com `json()` retornando `{"status": "ok"}` | Serviço retorna `[]`. |
| **TU08** | Propagação de erro HTTP ao ativar itens | Erros HTTP devem subir para o chamador | `raise_for_status` lança `HTTPError` | Chamada `ativar_itens_cardapio_unidade([1, 2])` | Lança `requests.HTTPError`. |
| **TU09** | Validação de lista de IDs vazia ao remover itens | Não deve permitir remoção com lista vazia | Lista de IDs vazia | Chamada `remover_itens_cardapio_unidade([])` | Lança `ValueError` sobre lista de IDs vazia. |
| **TU10** | Validação de IDs totalmente inválidos ao remover itens | Nenhum ID válido ⇒ erro de validação | Lista com valores não numéricos | Chamada `remover_itens_cardapio_unidade(["x", None, "y"])` | Lança `ValueError` indicando ausência de IDs válidos. |
| **TU11** | Conversão e limpeza de IDs ao remover itens | IDs inválidos devem ser ignorados | Resposta HTTP 200 simulada | Chamada `remover_itens_cardapio_unidade([10, "30", "a"])` com `requests.delete` mockado | JSON enviado é `{"itens": [10, 30]}` e retorno é lista com itens (`id` 10 e 30). |
| **TU12** | Propagação de erro HTTP ao remover itens | Erros HTTP devem ser propagados | `raise_for_status` lança erro | Chamada `remover_itens_cardapio_unidade([1, 2])` | Lança `requests.HTTPError`. |
| **TU13** | Cardápio central retornando lista válida | Serviço deve repassar lista corretamente | Resposta HTTP 200 simulada com lista | Chamada `listar_cardapio_central()` com `requests.get` mockado | Retorna lista com itens, incluindo `COMIDA == "X-Burger"` no segundo elemento. |
| **TU14** | Cardápio central com JSON inválido | JSON não-lista ⇒ lista vazia | JSON simulado como dict | Chamada `listar_cardapio_central()` com `json()` retornando `{"erro": "formato inválido"}` | Retorna `[]`. |
| **TU15** | Listar pedidos ativos – fluxo feliz (fila) | Serviço de fila deve retornar pedidos válidos | Resposta HTTP 200 simulada | Chamada `PedidosFilaService.listar_pedidos_ativos()` com `requests.get` mockado | Retorna lista com um pedido contendo `NUMERO_PEDIDO`, `NOME_CLIENTE`, `COMIDAS` etc., com valores esperados. |
| **TU16** | Listar pedidos ativos – erro HTTP (fila) | Erros do servidor devem ser propagados | `raise_for_status` lança `HTTPError` | Chamada `listar_pedidos_ativos()` | Lança `requests.HTTPError`. |
| **TU17** | Conversão de reais para centavos – valor inteiro | Conversão exata de reais para centavos em string | Instância de `RealizarPedidoService` | Chamada `_reais_para_centavos_str(10.0)` | Retorna `"1000"`. |
| **TU18** | Conversão de reais para centavos – arredondamento para cima | Arredondamento correto de valores decimais | Serviço instanciado | Chamada `_reais_para_centavos_str(10.999)` | Retorna `"1100"`. |
| **TU19** | Conversão de reais para centavos – arredondamento normal | Arredondamento correto em casos comuns | Serviço instanciado | Chamada `_reais_para_centavos_str(10.235)` | Retorna `"1024"`. |
| **TU20** | Conversão de reais para centavos – zero reais | Zero deve ser tratado adequadamente | Serviço instanciado | Chamada `_reais_para_centavos_str(0.0)` | Retorna `"0"`. |
| **TU21** | Criar pedido – payload completo e retorno válido | Payload JSON deve ser montado corretamente | Backend simulando retorno `{"status": "ok", "id": 123}` | Chamada `criar_pedido(numero_pedido="1001", nome_cliente="João Silva", cpf="11122233344", comidas=["X-BURGUER", "REFRIGERANTE"], preco_total_reais=21.0, tempo_preparo_total_min=12)` | URL chamada é `/pedidos`, JSON enviado contém número, nome, CPF, comidas concatenadas, preço `"2100"`, tempo `"12"`; retorno igual ao JSON simulado. |
| **TU22** | Criar pedido – JSON vazio ou nulo | JSON `None` deve resultar em dict vazio | Backend retorna `None` em `json()` | Chamada `criar_pedido(...)` | Serviço retorna `{}`. |
| **TU23** | Criar pedido – erro HTTP | Erros do backend devem ser propagados | `raise_for_status` lança `HTTPError` | Chamada `criar_pedido(...)` com dados simples | Lança `requests.HTTPError`. |
| **TU24** | Criar pedido – normalização do número do pedido | Zeros à esquerda devem ser removidos | Backend 200 simulando resposta ok | Chamada `criar_pedido(numero_pedido="0010", ...)` | JSON enviado possui `"NUMERO_PEDIDO": "10"`, preço convertido `"950"` e tempo `"7"`. |
| **TU25** | Listar pedidos ativos (RealizarPedidoService) – JSON lista válida | Deve retornar lista de pedidos ativos | Resposta HTTP 200 com lista | Chamada `RealizarPedidoService.listar_pedidos_ativos()` | Retorna lista com dois itens (`NUMERO_PEDIDO` `"1001"` e `"1002"`). |
| **TU26** | Listar pedidos ativos – JSON não-lista | JSON inválido ⇒ lista vazia | Backend retorna dict | Chamada `listar_pedidos_ativos()` | Retorna `[]`. |
| **TU27** | Listar pedidos ativos – erro HTTP | Erro deve ser propagado | `raise_for_status` lança `HTTPError` | Chamada `listar_pedidos_ativos()` | Lança `requests.HTTPError`. |
| **TU28** | Listar pedidos ativos – JSON `None` | Ausência de dados ⇒ lista vazia | `json()` retorna `None` | Chamada `listar_pedidos_ativos()` | Retorna `[]`. |
| **TU29** | Atualizar status de pedidos – JSON dict válido | Resposta dict deve ser retornada diretamente | Backend retorna `{"atualizados": 3}` | Chamada `atualizar_status_pedidos()` | Retorna `{"atualizados": 3}`. |
| **TU30** | Atualizar status de pedidos – JSON não-dict | JSON inválido ⇒ dict vazio | `json()` retorna lista | Chamada `atualizar_status_pedidos()` | Retorna `{}`. |
| **TU31** | Atualizar status de pedidos – erro HTTP | Erros devem ser propagados | `raise_for_status` lança `HTTPError` | Chamada `atualizar_status_pedidos()` | Lança `requests.HTTPError`. |
| **TU32** | Listar histórico – fluxo feliz | Histórico deve retornar lista válida | Backend 200 com lista simulada | Chamada `HistoricoService.listar_historico()` com `requests.get` mockado | Retorna lista com um pedido histórico (`NUMERO_PEDIDO` `"2001"`, `NOME_CLIENTE` `"Maria Oliveira"`). |
| **TU33** | Listar histórico – erro HTTP | Erro deve ser propagado | `raise_for_status` lança `HTTPError` | Chamada `listar_historico()` | Lança `requests.HTTPError`. |
| **TU34** | Visualizar cardápio da unidade – fluxo feliz | Conversão de preço (centavos → reais) e estrutura final | Backend 200 com lista de itens | Chamada `VisualizarCardapioService.view_menu()` com `json()` retornando itens com `PRECO` `"2100"` e `"500"` | Lista final possui dois itens, com nomes, preços `21.0` e `5.0`, e tempos de preparo corretos. |
| **TU35** | Visualizar cardápio da unidade – dados inválidos | Aplicação de valores default em campos ausentes/invalidos | Backend retorna itens com campos faltando ou `PRECO` inválido | Chamada `view_menu()` com JSON contendo itens incompletos | Cada item resultante sempre possui `nome`, `preco` e `tempo_preparo`, usando `"Sem nome"`, `0.0` e `"N/A"` como defaults quando necessário. |
| **TU36** | Listar notas fiscais – fluxo feliz | Conversão de preço e retorno consistente | Backend 200 com lista de notas | Chamada `VisualizarNotasFiscaisService.listar_notas_fiscais()` | Retorna lista com notas contendo `NUMERO_PEDIDO`, `NOME_CLIENTE`, `CPF` corretos e `PRECO` convertido para `21.0` e `17.0`. |
| **TU37** | Listar notas fiscais – dados inválidos | Campos faltantes/inválidos devem usar defaults | Backend retorna nota com `PRECO` inválido e outra completamente vazia | Chamada `listar_notas_fiscais()` | Primeiro item mantém dados de pedido/cliente, mas `PRECO` vira `0.0`; segundo item usa `"N/A"` para `NUMERO_PEDIDO`, `NOME_CLIENTE`, `CPF` e `0.0` para `PRECO`. |

---

## Resumo Geral

- **Todos os testes unitários executados foram aprovados.**
- A suíte valida:
  - Tratamento correto de **sucesso** e **falha** (HTTP 200 vs erros HTTP).
  - **Validação de entrada** (listas vazias, IDs inválidos, JSON malformado).
  - **Conversões numéricas** (reais ↔ centavos).
  - **Normalização de dados** (número de pedido, listas de itens, defaults em campos ausentes).
  - Comportamento consistente entre serviços de **cardápio**, **pedidos**, **fila**, **histórico** e **notas fiscais**.

O sistema demonstra comportamento robusto, previsível e alinhado às regras de negócio definidas para o Burguer FEI.