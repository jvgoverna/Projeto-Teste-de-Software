# Testes Funcionais de Caixa Branca – Sistema de Pedidos

Este documento descreve o conjunto de testes funcionais de caixa branca implementados diretamente sobre os serviços do sistema de pedidos (módulos de cardápio, fila de preparo, histórico e notas fiscais), com base no relatório de cobertura apresentado (97% de cobertura total).

# Objetivo dos testes

Os testes de caixa branca têm como objetivo verificar se:

As regras de negócio internas de cada serviço estão corretas, exercitando diferentes caminhos e condições do código.

As funções e métodos públicos de cada serviço retornam os valores esperados para entradas válidas e inválidas.

A maior parte dos ramos de decisão foi executada, garantindo alta cobertura de código.

Chamadas externas (como requisições HTTP para API de cardápio) podem ser testadas de forma isolada, utilizando monkeypatch para simular respostas.

# Resultado da execução dos testes de caixa branca

📊 Cobertura de código geral: `97% (119 comandos, 4 não exercitados, 18 branches analisados)`.

Por módulo de serviço:

`src/services/editar_itens_cardapio_service.py` – 43 statements, 0 faltando → 100% de cobertura

`src/services/pedidos_fila_service.py` – 8 statements, 0 faltando → 100% de cobertura

`src/services/realizar_pedido_service.py` – 21 statements, 4 faltando → 83% de cobertura

`src/services/visualizar_cardapio_service.py` – 18 statements, 0 faltando → 100% de cobertura

`src/services/visualizar_historico_service.py` – 9 statements, 0 faltando → 100% de cobertura

`src/services/visualizar_notas_fiscais_service.py` – 20 statements, 0 faltando → 100% de cobertura

# ✅ Interpretação geral

A grande maioria das regras de negócio dos serviços foi exercitada pelos testes, principalmente nos módulos de edição de cardápio, fila de pedidos, visualização de cardápio, histórico e notas fiscais, todos com 100% de cobertura.

O módulo RealizarPedidoService ainda possui 4 linhas não cobertas (83%), indicando cenários de borda que podem ser explorados em testes futuros (por exemplo: validações específicas, tratamentos de erro ou caminhos alternativos do fluxo de criação de pedido).

🛠️ Uso de monkeypatch (testes de caixa branca com simulação de APIs)

Nos testes foram utilizados o monkeypatch do pytest para substituir chamadas reais à API de cardápio (por exemplo, requests.get e requests.post) por funções falsas (fakes) que retornam dados controlados.

Isso permitiu:

Testar somente a lógica interna dos serviços (condições, laços, tratamento de listas, etc.), sem depender de uma API externa ou de rede.

Garantir reprodutibilidade dos testes, com respostas previsíveis e estáveis.

Aumentar a cobertura de código, exercitando cenários que seriam difíceis de reproduzir apenas com a API real.

# Comando para rodar os testes funcionais de Caixa Branca:
**Obs.: rode o comando na pasta raíz do projeto**
Esse comando executa todos os testes funcionais de caixa branca, gera o relatório de cobertura em HTML e abre automaticamente o arquivo no seu navegador padrão.

PYTHONPATH=. pytest "tests/functional" \
  --cov=src.services.realizar_pedido_service \
  --cov=src.services.pedidos_fila_service \
  --cov=src.services.editar_itens_cardapio_service\
  --cov=src.services.visualizar_cardapio_service\
  --cov=src.services.visualizar_notas_fiscais_service\
  --cov=src.services.visualizar_historico_service\
  --cov-branch \
  --cov-report=html && xdg-open htmlcov/index.html

## Obs.: É obrigatório estar com o banco de dados e a API ativos

### Passo a passo para subir a API antes de rodar os testes

1. Abra um terminal na sua máquina.
2. Vá até a pasta `src` do projeto: `cd ~/Documentos/GitHub/Projeto-Teste-de-Software/src`
3. Rode o comando: `uvicorn Server.BurgerFeiAPI:app --reload --port 8000`
