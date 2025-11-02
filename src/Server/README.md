# API da Lanchonete

API de POC para gerenciar um cardápio central, ativação de itens por unidade e visualização de dados. Projetada para ser didática e fácil de manter.

# Base URL


| URL | Description |
|-----|-------------|


# APIs

## GET /health

Healthcheck

VERIFICA SE A APLICAÇÃO ESTÁ NO AR
----------------------------------
Retorna um JSON simples com `{"status": "ok"}`.

Quando usar?
------------
- Para monitoramento básico (liveness probe).
- Para checar rapidamente se o servidor subiu.




### Responses

#### 200


Successful Response








## GET /db/ping

Ping Db

TESTA UMA CONSULTA SIMPLES AO BANCO
-----------------------------------
Executa `SELECT 1` no SQLite para verificar se a conexão está viva.

Respostas possíveis:
--------------------
- 200 OK: `{ "db": "connected", "path": ".../lanchonete.db" }`
- 500: falha ao consultar o SQLite.




### Responses

#### 200


Successful Response








## GET /_debug/db/dump

Show All Tables

MOSTRA O CONTEÚDO DE TODAS AS TABELAS (DEBUG)
---------------------------------------------
Lista todas as tabelas do SQLite (exceto internas) e devolve um dicionário onde
cada chave é o nome da tabela e o valor é a lista de registros.

Quando usar?
------------
- Durante o desenvolvimento para validar rapidamente o estado do banco.
- Não é uma rota de produção para sistemas reais (apenas debug).

Exemplo de resposta:
--------------------
{
  "CARDAPIO_CENTRAL": [
    {"id": 1, "COMIDA": "HAMBURGUER", "PRECO": "1500", "TEMPO_PREPARO": "10"},
    ...
  ],
  "CARDAPIO_UNIDADE": []
}




### Responses

#### 200


Successful Response








## PUT /cardapio/unidade/itens

Atualizar Itens Do Cardapio Da Unidade

ATUALIZAR ITENS DO CARDÁPIO DA UNIDADE (PARCIAL, LOTE)
======================================================

Objetivo:
----------
Atualizar parcialmente registros de `CARDAPIO_UNIDADE` informando o `id` e os campos a mudar.

Regras:
--------
- O corpo deve conter `itens` (lista).
- Cada item deve ter `id` (int) e pelo menos um dentre: `COMIDA`, `PRECO`, `TEMPO_PREPARO`.
- Para cada atualização bem-sucedida, o registro atualizado é lido e retornado em `itens_atualizados`.

Exemplo de requisição:
----------------------
PUT /cardapio/unidade/itens
{
  "itens": [
    { "id": 3, "COMIDA": "X-BURGUER_DOBRO", "PRECO": "1900" },
    { "id": 5, "TEMPO_PREPARO": "9" }
  ]
}

Exemplo de resposta:
--------------------
{
  "quantidade_de_itens_atualizados": 2,
  "lista_de_erros_durante_atualizacao": [],
  "itens_atualizados": [
    {"id":3,"COMIDA":"X-BURGUER_DOBRO","PRECO":"1900","TEMPO_PREPARO":"10"},
    {"id":5,"COMIDA":"X-SALADA","PRECO":"1600","TEMPO_PREPARO":"9"}
  ]
}

Observação:
------------
Esta rota substitui a antiga `/db/unidade/atualizar` para manter consistência REST.




### Request Body

object







### Responses

#### 200


Successful Response








#### 422


Validation Error


[HTTPValidationError](#httpvalidationerror)







## POST /cardapio/unidade/itens

Ativar Itens Do Cardapio Da Unidade

ATIVAR ITENS DO CARDÁPIO CENTRAL NA UNIDADE (LOTE)
==================================================

Objetivo:
----------
A partir de uma lista de IDs (inteiros) da tabela `CARDAPIO_CENTRAL`, o servidor copia
os registros correspondentes para a tabela `CARDAPIO_UNIDADE`.  
Isso representa “ativar” itens disponíveis para venda naquela unidade.

Regras:
--------
- O campo `itens` deve existir no corpo JSON e conter uma lista de inteiros.
- Se um ID não existir no `CARDAPIO_CENTRAL`, um erro será registrado, mas o processo continua.
- Nenhum item é removido; apenas novos registros são adicionados à unidade.

Exemplo de requisição:
----------------------
POST /cardapio/unidade/itens
{
  "itens": [1, 2, 4, 6]
}

Exemplo de resposta:
--------------------
{
  "quantidade_de_itens_ativados": 3,
  "lista_de_erros_durante_ativacao": [
    { "id": "6", "erro": "Item não encontrado no CARDAPIO_CENTRAL" }
  ]
}

Observação:
------------
Essa rota substitui a antiga `/db/unidade/ativar` para seguir uma convenção REST mais clara.




### Request Body

object







### Responses

#### 200


Successful Response








#### 422


Validation Error


[HTTPValidationError](#httpvalidationerror)







## DELETE /cardapio/unidade/itens

Remover Itens Do Cardapio Da Unidade

REMOVER ITENS DO CARDÁPIO DA UNIDADE (LOTE)
===========================================

Objetivo:
----------
Remover, em lote, registros de `CARDAPIO_UNIDADE` informando seus IDs (inteiros).

Regras:
--------
- O corpo deve conter `itens` como lista de inteiros.
- Para cada ID, tenta-se remover; falhas são registradas e o processamento continua.

Exemplo de requisição (curl):
-----------------------------
curl -X DELETE http://127.0.0.1:8000/cardapio/unidade/itens \
  -H "Content-Type: application/json" \
  -d '{"itens":[2,4,6]}'

Exemplo de resposta:
--------------------
{
  "quantidade_de_itens_removidos": 2,
  "lista_de_erros_durante_remocao": [
    { "id": "6", "erro": "Falha ao remover do CARDAPIO_UNIDADE: ..." }
  ]
}

Observação:
------------
Esta rota substitui a antiga `/db/unidade/remover` para seguir convenções REST mais claras.




### Request Body

object







### Responses

#### 200


Successful Response








#### 422


Validation Error


[HTTPValidationError](#httpvalidationerror)







## POST /pedidos

Adicionar Pedido Formatado Unico

CRIAR PEDIDO (ÚNICO) E GERAR NOTA FISCAL
========================================

Objetivo
--------
Criar **um** registro em `PEDIDOS_ATIVOS` (o servidor preenche `HORARIO_ADICIONADO` com epoch seconds)
e gerar a respectiva nota em `NOTAS_FISCAIS`.

Regras de entrada
-----------------
Envie um JSON com os campos obrigatórios:
- `NUMERO_PEDIDO` (string)
- `NOME_CLIENTE` (string)
- `CPF` (string)
- `COMIDAS` (string agregado, separado por vírgula)
- `PRECO` (string com valor em centavos, ex.: "2100")
- `TEMPO_PREPARO` (string; **nesta POC é interpretado como segundos**)

Comportamento
-------------
1) Valida os campos obrigatórios.
2) Insere o pedido em `PEDIDOS_ATIVOS` preenchendo `HORARIO_ADICIONADO` (epoch seconds).
3) Insere a nota fiscal em `NOTAS_FISCAIS` (`NUMERO_PEDIDO`, `NOME_CLIENTE`, `CPF`, `PRECO`).
4) Retorna os IDs gerados.

Exemplos
--------
Requisição:
POST /pedidos
{
  "NUMERO_PEDIDO": "1003",
  "NOME_CLIENTE": "Carlos Mendes",
  "CPF": "11122233344",
  "COMIDAS": "HAMBURGUER, REFRIGERANTE",
  "PRECO": "2100",
  "TEMPO_PREPARO": "11"
}

Resposta (201):
{
  "mensagem": "Pedido e nota fiscal inseridos com sucesso.",
  "id_pedido_inserido": 7,
  "id_nota_fiscal_inserida": 7
}

Observações
-----------
- Se o pedido for salvo mas a nota fiscal falhar, retornamos 201 com aviso e `erro_nota_fiscal`,
  para que a emissão da NF possa ser tentada novamente posteriormente.




### Request Body

object







### Responses

#### 200


Successful Response








#### 422


Validation Error


[HTTPValidationError](#httpvalidationerror)







## POST /pedidos/atualizar-status

Atualizar Pedidos Ativos Movendo Para Historico

ATUALIZAR STATUS DOS PEDIDOS ATIVOS → MOVER PRONTOS PARA HISTÓRICO
==================================================================

Objetivo
--------
Ler todos os registros de `PEDIDOS_ATIVOS`, verificar se o tempo decorrido desde
`HORARIO_ADICIONADO` já atingiu `TEMPO_PREPARO` (nesta POC, em **segundos**)
e, quando atingido, mover o pedido para `HISTORICO_PEDIDOS`, removendo-o de `PEDIDOS_ATIVOS`.

Regras (POC)
------------
- `TEMPO_PREPARO` é tratado como **segundos** (ex.: "10" = 10s).
- `HORARIO_ADICIONADO` é salvo como epoch seconds (string) no momento da criação do pedido.
- Em caso de falha ao inserir no histórico, o item **não** é removido dos ativos.

Retorno
-------
200 OK
{
  "quantidade_movidos_para_historico": <int>,
  "ids_movidos_para_historico": [<ids de PEDIDOS_ATIVOS>],
  "erros": [
    {"id": "7", "erro": "Falha ao remover de PEDIDOS_ATIVOS: ..."},
    ...
  ],
  "resumo_ainda_ativos": [
    { "id": "8", "NUMERO_PEDIDO": "1004", "faltam_segundos": "3" },
    ...
  ]
}

Exemplo
-------
Requisição:
  POST /pedidos/atualizar-status

Possíveis cenários:
- Se o pedido estiver pronto, ele é copiado para `HISTORICO_PEDIDOS` e removido de `PEDIDOS_ATIVOS`.
- Se ainda não estiver pronto, ele permanece em `PEDIDOS_ATIVOS` e é listado em `resumo_ainda_ativos`.




### Responses

#### 200


Successful Response








## GET /cardapio/central

Listar Cardapio Central

LISTAR CARDÁPIO CENTRAL (CATÁLOGO GERAL)
========================================

Objetivo
--------
Retornar todos os registros da tabela `CARDAPIO_CENTRAL`, que representa o catálogo
geral de produtos (seed inicial carregado via JSON).

Estrutura
----------
- Tabela: `CARDAPIO_CENTRAL`
- Colunas: COMIDA, PRECO, TEMPO_PREPARO

Exemplo
--------
GET /cardapio/central

Resposta (200):
[
  { "id": 1, "COMIDA": "HAMBURGUER", "PRECO": "1500", "TEMPO_PREPARO": "10" },
  { "id": 2, "COMIDA": "BATATA FRITA", "PRECO": "800", "TEMPO_PREPARO": "5" }
]




### Responses

#### 200


Successful Response








## GET /cardapio/unidade

Listar Cardapio Unidade

LISTAR CARDÁPIO DA UNIDADE (ITENS ATIVOS)
=========================================

Objetivo
--------
Retornar os itens atualmente ativos e disponíveis para venda na unidade
(`CARDAPIO_UNIDADE`).

Estrutura
----------
- Tabela: `CARDAPIO_UNIDADE`
- Colunas: COMIDA, PRECO, TEMPO_PREPARO

Exemplo
--------
GET /cardapio/unidade

Resposta (200):
[
  { "id": 3, "COMIDA": "X-BURGUER", "PRECO": "1700", "TEMPO_PREPARO": "8" },
  { "id": 4, "COMIDA": "REFRIGERANTE", "PRECO": "600", "TEMPO_PREPARO": "1" }
]




### Responses

#### 200


Successful Response








## GET /pedidos/ativos

Listar Pedidos Ativos

LISTAR PEDIDOS ATIVOS (EM PREPARO)
==================================

Objetivo
--------
Retornar todos os pedidos ainda em preparo ou aguardando conclusão,
armazenados na tabela `PEDIDOS_ATIVOS`.

Estrutura
----------
- Tabela: `PEDIDOS_ATIVOS`
- Colunas: NUMERO_PEDIDO, NOME_CLIENTE, CPF, COMIDAS, PRECO, TEMPO_PREPARO, HORARIO_ADICIONADO

Exemplo
--------
GET /pedidos/ativos

Resposta (200):
[
  {
    "id": 1,
    "NUMERO_PEDIDO": "1001",
    "NOME_CLIENTE": "João Silva",
    "CPF": "11122233344",
    "COMIDAS": "X-BURGUER, REFRIGERANTE",
    "PRECO": "2100",
    "TEMPO_PREPARO": "12",
    "HORARIO_ADICIONADO": "1730472103"
  }
]




### Responses

#### 200


Successful Response








## GET /pedidos/historico

Listar Historico Pedidos

LISTAR HISTÓRICO DE PEDIDOS (CONCLUÍDOS)
========================================

Objetivo
--------
Retornar os pedidos já concluídos e movidos de `PEDIDOS_ATIVOS` para `HISTORICO_PEDIDOS`.

Estrutura
----------
- Tabela: `HISTORICO_PEDIDOS`
- Colunas: NUMERO_PEDIDO, NOME_CLIENTE, CPF, COMIDAS, PRECO, TEMPO_PREPARO, HORARIO_ADICIONADO

Exemplo
--------
GET /pedidos/historico

Resposta (200):
[
  {
    "id": 5,
    "NUMERO_PEDIDO": "1002",
    "NOME_CLIENTE": "Maria Oliveira",
    "CPF": "99988877766",
    "COMIDAS": "BATATA FRITA, SUCO",
    "PRECO": "1700",
    "TEMPO_PREPARO": "6",
    "HORARIO_ADICIONADO": "1730471500"
  }
]




### Responses

#### 200


Successful Response








## GET /notas-fiscais

Listar Notas Fiscais

LISTAR NOTAS FISCAIS EMITIDAS
=============================

Objetivo
--------
Retornar todas as notas fiscais registradas em `NOTAS_FISCAIS`,
correspondentes aos pedidos inseridos.

Estrutura
----------
- Tabela: `NOTAS_FISCAIS`
- Colunas: NUMERO_PEDIDO, NOME_CLIENTE, CPF, PRECO

Exemplo
--------
GET /notas-fiscais

Resposta (200):
[
  { "id": 1, "NUMERO_PEDIDO": "1001", "NOME_CLIENTE": "João Silva", "CPF": "11122233344", "PRECO": "2100" },
  { "id": 2, "NUMERO_PEDIDO": "1002", "NOME_CLIENTE": "Maria Oliveira", "CPF": "99988877766", "PRECO": "1700" }
]




### Responses

#### 200


Successful Response








# Components



## HTTPValidationError



| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |


## ValidationError



| Field | Type | Description |
|-------|------|-------------|
| loc | array |  |
| msg | string |  |
| type | string |  |
