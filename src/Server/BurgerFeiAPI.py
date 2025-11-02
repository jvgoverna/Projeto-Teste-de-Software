# Server/BurgerFeiAPI.py
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

from fastapi import Body, Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse

from SQLLiteManager.SQLLiteManager import SQLLiteManager

"""
API DA LANCHONETE — DOCUMENTAÇÃO GERAL (POC)
============================================

PROPÓSITO
---------
Esta POC demonstra um backend simples para lanchonete com:
- **FastAPI** expondo endpoints REST claros e consistentes;
- **SQLite** (arquivo local) para persistência de dados;
- Fluxos didáticos de **cardápio**, **pedidos** e **notas fiscais**.

A ideia é ser fácil de ler, testar e manter. O esquema é minimalista (tudo TEXT),
mas cobre o ciclo essencial: cadastrar itens ativos na unidade, registrar pedidos
e acompanhar seu estado até o histórico, emitindo nota fiscal.

VISÃO GERAL DOS RECURSOS
------------------------
Infra / Saúde
- `GET /health`
  - *Liveness probe*. Útil para checar se a aplicação está de pé.
- `GET /db/ping`
  - Testa a conectividade com o SQLite via `SELECT 1`.
- `GET /_debug/db/dump`
  - Retorna o conteúdo de todas as tabelas (somente para desenvolvimento/debug).

Cardápio
- Seed do **cardápio central** carregado via JSON no startup (apenas se vazio).
- `GET /cardapio/central`
  - Lista o catálogo geral (tabela `CARDAPIO_CENTRAL`).
- `POST /cardapio/unidade/itens`
  - **Ativa** itens na unidade copiando do cardápio central (lote).
  - Corpo: `{ "itens": [<ids de CARDAPIO_CENTRAL>] }`.
- `DELETE /cardapio/unidade/itens`
  - **Remove** itens ativos da unidade por IDs (lote).
  - Corpo: `{ "itens": [<ids de CARDAPIO_UNIDADE>] }`.
- `PUT /cardapio/unidade/itens`
  - **Atualiza parcialmente** itens da unidade (lote).
  - Campos permitidos: `COMIDA`, `PRECO`, `TEMPO_PREPARO`.

Pedidos
- `POST /pedidos`
  - Cria **um** pedido já agregado (`COMIDAS` como string separada por vírgulas),
    o servidor preenche `HORARIO_ADICIONADO` (epoch seconds) e registra a **nota fiscal**
    (`NOTAS_FISCAIS`) com `NUMERO_PEDIDO`, `NOME_CLIENTE`, `CPF`, `PRECO`.
- `POST /pedidos/atualizar-status`
  - Varre `PEDIDOS_ATIVOS` e move para `HISTORICO_PEDIDOS` os que já “venceram” o tempo de preparo.
  - **Nesta POC `TEMPO_PREPARO` é interpretado como segundos**.

ESQUEMA DE DADOS (RESUMO)
-------------------------
- **CARDAPIO_CENTRAL** — catálogo geral (seed via JSON)
  - Colunas: `COMIDA`, `PRECO`, `TEMPO_PREPARO`
- **CARDAPIO_UNIDADE** — itens ativos da unidade
  - Colunas: `COMIDA`, `PRECO`, `TEMPO_PREPARO`
- **PEDIDOS_ATIVOS** — pedidos em preparo/aguardando
  - Colunas: `NUMERO_PEDIDO`, `NOME_CLIENTE`, `CPF`, `COMIDAS`, `PRECO`, `TEMPO_PREPARO`, `HORARIO_ADICIONADO`
- **HISTORICO_PEDIDOS** — pedidos concluídos
  - Colunas: `NUMERO_PEDIDO`, `NOME_CLIENTE`, `CPF`, `COMIDAS`, `PRECO`, `TEMPO_PREPARO`, `HORARIO_ADICIONADO`
- **NOTAS_FISCAIS** — registro de NF emitida
  - Colunas: `NUMERO_PEDIDO`, `NOME_CLIENTE`, `CPF`, `PRECO`

COMO EXECUTAR
-------------
1) Subir o servidor (hot-reload):
   uvicorn Server.BurgerFeiAPI:app --reload --port 8000

2) Abrir a documentação interativa (Swagger UI):
   http://127.0.0.1:8000/docs

EXEMPLOS RÁPIDOS
----------------
Infra
- Health:                  GET /health
- Ping banco:              GET /db/ping
- Dump (debug):            GET /_debug/db/dump

Cardápio
- Cardápio central:        GET /cardapio/central
- Ativar itens (lote):     POST /cardapio/unidade/itens
                           Body: { "itens": [1, 2, 3] }
- Remover itens (lote):    DELETE /cardapio/unidade/itens
                           Body: { "itens": [1, 4] }
- Atualizar itens (lote):  PUT /cardapio/unidade/itens
                           Body: { "itens": [
                             { "id": 3, "PRECO": "1800" },
                             { "id": 5, "TEMPO_PREPARO": "9" }
                           ] }

Pedidos
- Criar pedido + NF:       POST /pedidos
                           Body: {
                             "NUMERO_PEDIDO": "1003",
                             "NOME_CLIENTE": "Carlos Mendes",
                             "CPF": "11122233344",
                             "COMIDAS": "HAMBURGUER, REFRIGERANTE",
                             "PRECO": "2100",
                             "TEMPO_PREPARO": "11"
                           }
- Atualizar status:        POST /pedidos/atualizar-status
                           (move prontos de PEDIDOS_ATIVOS → HISTORICO_PEDIDOS)
"""

# Importa a classe do pacote SQLLiteManager (irmão de Server, ambos na raiz)
# Estrutura do projeto:
# PROJETO/
# ├── Database/
# ├── Server/
# │   └── BurgerFeiAPI.py
# └── SQLLiteManager/
#     └── SQLLiteManager.py

# === Caminhos importantes ===
BASE_DIR: Path = Path(__file__).resolve().parent.parent  # raiz do projeto (PROJETO/)
DATABASE_DIR: Path = BASE_DIR / "Database"
DATABASE_DIR.mkdir(parents=True, exist_ok=True)  # garante que a pasta existe

SQLITE_DB_PATH: Path = DATABASE_DIR / "lanchonete.db"
DEFAULT_CENTRAL_JSON: Path = DATABASE_DIR / "cardapio_central.json"

# Instância da aplicação FastAPI
app = FastAPI(
    title="API da Lanchonete",
    version="0.1.0",
    description=(
        "API de POC para gerenciar um cardápio central, ativação de itens por unidade e visualização de dados. "
        "Projetada para ser didática e fácil de manter."
    ),
)


# =====================================================================================
# Funções utilitárias internas (pequenas e diretas)
# =====================================================================================

def _as_path(valor: Union[str, Path]) -> Path:
    """
    Converte um valor (str ou Path) para Path.

    Por que isso existe?
    --------------------
    Em alguns pontos, podemos receber um caminho como string. Para padronizar o uso do
    módulo `pathlib`, convertemos para `Path`.

    Parâmetros:
    -----------
    valor : str | Path
        Caminho de arquivo/pasta.

    Retorno:
    --------
    Path
        O mesmo caminho como objeto `Path`.
    """
    return valor if isinstance(valor, Path) else Path(valor)


def _contar_registros(gerenciador_do_banco: SQLLiteManager, nome_tabela: str) -> int:
    """
    Conta quantos registros existem em uma tabela.

    Por que isso existe?
    --------------------
    Útil para saber, por exemplo, se uma tabela está vazia antes de fazer um seed/import.

    Regras:
    -------
    - O nome da tabela é validado pelo `SQLLiteManager` (somente letras/números/_).

    Parâmetros:
    -----------
    gerenciador_do_banco : SQLLiteManager
        Instância aberta do gerenciador (conexão ativa).
    nome_tabela : str
        Nome da tabela (ex.: "CARDAPIO_CENTRAL").

    Retorno:
    --------
    int
        Quantidade de registros.
    """
    if not gerenciador_do_banco.validar_nome_identificador_simples(nome_tabela):
        raise ValueError("Nome de tabela inválido para contagem.")

    cursor = gerenciador_do_banco.conexao_ativa_banco_sqlite.execute(
        f"SELECT COUNT(*) FROM {nome_tabela}"
    )
    quantidade = cursor.fetchone()[0]
    return int(quantidade)


def importar_cardapio_central_de_json(
    gerenciador_do_banco: SQLLiteManager,
    caminho_do_arquivo_json: Union[str, Path] = DEFAULT_CENTRAL_JSON
) -> int:
    """
    IMPORTA O CARDÁPIO CENTRAL A PARTIR DE UM ARQUIVO JSON NO DISCO
    =================================================================

    QUANDO É USADO?
    ---------------
    Chamado durante o *startup* do servidor. Ele só importa se a tabela
    `CARDAPIO_CENTRAL` estiver **vazia** (para evitar duplicações na POC).

    FORMATO DO JSON ESPERADO:
    -------------------------
    Uma lista de objetos, com os campos exatos abaixo (strings):
    [
      { "COMIDA": "HAMBURGUER", "PRECO": "1500", "TEMPO_PREPARO": "10" },
      { "COMIDA": "BATATA_FRITA", "PRECO": "800",  "TEMPO_PREPARO": "5"  },
      ...
    ]

    Parâmetros:
    -----------
    gerenciador_do_banco : SQLLiteManager
        Gerenciador com conexão ativa (app.state.db_manager).
    caminho_do_arquivo_json : str | Path
        Caminho do arquivo JSON no disco (por padrão: ./Database/cardapio_central.json).

    Retorno:
    --------
    int
        Quantidade de itens inseridos no `CARDAPIO_CENTRAL`.

    Erros comuns:
    -------------
    - HTTP 500 se o JSON não existir ou não puder ser lido.
    - HTTP 400 se faltar algum campo obrigatório no JSON.
    """
    nome_da_tabela_central = "CARDAPIO_CENTRAL"

    # 1) Verifica se a tabela já tem registros
    try:
        quantidade_existente = _contar_registros(gerenciador_do_banco, nome_da_tabela_central)
    except Exception as erro_contagem:
        raise HTTPException(status_code=500, detail=f"Falha ao contar registros de {nome_da_tabela_central}: {erro_contagem}")

    if quantidade_existente > 0:
        # Já tem dados: não importar novamente (evita duplicação nesta POC)
        return 0

    # 2) Verifica arquivo e lê JSON
    caminho_json = _as_path(caminho_do_arquivo_json)
    if not caminho_json.exists():
        raise HTTPException(
            status_code=500,
            detail=f"Arquivo JSON do cardápio central não encontrado: {caminho_json}"
        )

    try:
        with caminho_json.open("r", encoding="utf-8") as ponteiro_de_arquivo:
            lista_de_itens_json: List[Dict[str, Any]] = json.load(ponteiro_de_arquivo)
    except Exception as erro_leitura:
        raise HTTPException(status_code=500, detail=f"Falha ao ler JSON: {erro_leitura}")

    # 3) Valida e insere cada item no banco (tabela CARDAPIO_CENTRAL)
    colunas_obrigatorias = ["COMIDA", "PRECO", "TEMPO_PREPARO"]
    quantidade_inserida = 0

    for item_unico in lista_de_itens_json:
        # Valida campos exigidos
        try:
            valor_comida = str(item_unico["COMIDA"])
            valor_preco = str(item_unico["PRECO"])
            valor_tempo = str(item_unico["TEMPO_PREPARO"])
        except KeyError as falta:
            raise HTTPException(status_code=400, detail=f"JSON inválido. Campo ausente: {falta}")

        # Tenta inserir no banco
        try:
            gerenciador_do_banco.adicionar_registro_na_tabela(
                nome_da_tabela=nome_da_tabela_central,
                lista_de_nomes_de_colunas=colunas_obrigatorias,
                lista_de_valores_para_inserir=[valor_comida, valor_preco, valor_tempo],
            )
            quantidade_inserida += 1
        except Exception as erro_insercao:
            # Nesta POC, falhamos explicitamente para visibilidade
            raise HTTPException(status_code=500, detail=f"Falha ao inserir item no {nome_da_tabela_central}: {erro_insercao}")

    return quantidade_inserida


# =====================================================================================
# Inicialização e encerramento do app (ciclo de vida)
# =====================================================================================

def startup_db() -> None:
    """
    CRIA TODAS AS TABELAS E IMPORTA O CARDÁPIO INICIAL (SE NECESSÁRIO)
    ==================================================================

    O que esta função faz:
    ----------------------
    1) Garante que as tabelas básicas existam (CREATE TABLE IF NOT EXISTS).
    2) Importa os itens do CARDÁPIO CENTRAL a partir do JSON (seed) caso a
       tabela esteja vazia.

    Por que fazemos isso no startup?
    --------------------------------
    Para que o ambiente de testes esteja pronto automaticamente, sem etapas manuais.
    """
    gerenciador: SQLLiteManager = getattr(app.state, "db_manager", None)
    if gerenciador is None:
        raise HTTPException(status_code=500, detail="DB manager não inicializado no app.state.db_manager")

    # Definição do esquema simples
    tabelas: List[Tuple[str, List[str], List[str]]] = [
        ("CARDAPIO_CENTRAL",  ["COMIDA", "PRECO", "TEMPO_PREPARO"],                        ["TEXT", "TEXT", "TEXT"]),
        ("CARDAPIO_UNIDADE",  ["COMIDA", "PRECO", "TEMPO_PREPARO"],                        ["TEXT", "TEXT", "TEXT"]),
        ("PEDIDOS_ATIVOS",    ["NUMERO_PEDIDO", "NOME_CLIENTE", "CPF", "COMIDAS", "PRECO", "TEMPO_PREPARO", "HORARIO_ADICIONADO"], ["TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT"]),
        ("HISTORICO_PEDIDOS", ["NUMERO_PEDIDO", "NOME_CLIENTE", "CPF", "COMIDAS", "PRECO", "TEMPO_PREPARO", "HORARIO_ADICIONADO"], ["TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT"]),
        ("NOTAS_FISCAIS",     ["NUMERO_PEDIDO", "NOME_CLIENTE", "CPF", "PRECO"],                            ["TEXT", "TEXT", "TEXT", "TEXT"]),
    ]

    # 1) Cria tabelas
    for nome_tabela, colunas, tipos in tabelas:
        gerenciador.criar_tabela_generica(
            nome_da_tabela=nome_tabela,
            lista_de_nomes_de_colunas=colunas,
            lista_de_tipos_de_colunas=tipos
        )

    # 2) Importa o seed do cardápio central (se vazio)
    quantidade_seed = importar_cardapio_central_de_json(gerenciador, DEFAULT_CENTRAL_JSON)
    if quantidade_seed:
        print(f"[OK] Seed CARDAPIO_CENTRAL carregado do JSON ({quantidade_seed} itens).")
    else:
        print("[OK] CARDAPIO_CENTRAL já possuía itens. Nenhum seed aplicado.")


@app.on_event("startup")
def on_startup() -> None:
    """
    EVENTO DE STARTUP (INÍCIO DO SERVIDOR)
    --------------------------------------
    - Abre a conexão com o SQLite (arquivo em ./Database/lanchonete.db).
    - Salva o gerenciador em `app.state.db_manager`.
    - Chama `startup_db()` para garantir tabelas e import inicial.
    """
    gerenciador = SQLLiteManager(str(SQLITE_DB_PATH))  # aceita str no construtor
    gerenciador.abrir_conexao_com_banco_sqlite()
    app.state.db_manager = gerenciador
    startup_db()


@app.on_event("shutdown")
def on_shutdown() -> None:
    """
    EVENTO DE SHUTDOWN (ENCERRAMENTO DO SERVIDOR)
    ---------------------------------------------
    Fecha a conexão com o SQLite com segurança.
    """
    gerenciador: SQLLiteManager = getattr(app.state, "db_manager", None)
    if gerenciador is not None:
        gerenciador.fechar_conexao_com_banco_sqlite()


def get_db() -> SQLLiteManager:
    """
    DEPENDENCY PARA INJETAR O GERENCIADOR DE BANCO NOS ENDPOINTS
    ------------------------------------------------------------
    Mantém as rotas limpas e permite trocar a implementação no futuro.
    """
    gerenciador: SQLLiteManager = getattr(app.state, "db_manager", None)
    if gerenciador is None:
        raise HTTPException(status_code=500, detail="Banco de dados não inicializado.")
    return gerenciador


# =====================================================================================
# ROTAS DE INFRA/SAÚDE
# =====================================================================================

@app.get("/health", tags=["infra"])
def healthcheck() -> JSONResponse:
    """
    VERIFICA SE A APLICAÇÃO ESTÁ NO AR
    ----------------------------------
    Retorna um JSON simples com `{"status": "ok"}`.

    Quando usar?
    ------------
    - Para monitoramento básico (liveness probe).
    - Para checar rapidamente se o servidor subiu.
    """
    return JSONResponse({"status": "ok"})


@app.get("/db/ping", tags=["infra"])
def ping_db(gerenciador_do_banco: SQLLiteManager = Depends(get_db)) -> JSONResponse:
    """
    TESTA UMA CONSULTA SIMPLES AO BANCO
    -----------------------------------
    Executa `SELECT 1` no SQLite para verificar se a conexão está viva.

    Respostas possíveis:
    --------------------
    - 200 OK: `{ "db": "connected", "path": ".../lanchonete.db" }`
    - 500: falha ao consultar o SQLite.
    """
    try:
        gerenciador_do_banco.conexao_ativa_banco_sqlite.execute("SELECT 1").fetchone()
        return JSONResponse({
            "db": "connected",
            "path": gerenciador_do_banco.caminho_completo_arquivo_banco_sqlite
        })
    except Exception as erro_ping:
        raise HTTPException(status_code=500, detail=f"Falha ao consultar o banco: {erro_ping}")


@app.get("/_debug/db/dump", tags=["infra"])
def show_all_tables(gerenciador_do_banco: SQLLiteManager = Depends(get_db)) -> JSONResponse:
    """
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
    """
    try:
        cursor = gerenciador_do_banco.conexao_ativa_banco_sqlite.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';"
        )
        lista_de_nomes_de_tabelas = [linha[0] for linha in cursor.fetchall()]

        dicionario_resultado: Dict[str, Any] = {}
        for nome_de_tabela in lista_de_nomes_de_tabelas:
            try:
                registros = gerenciador_do_banco.ler_todos_os_registros_da_tabela(nome_de_tabela)
                dicionario_resultado[nome_de_tabela] = registros
            except Exception as erro_leitura:
                dicionario_resultado[nome_de_tabela] = {"erro": f"Erro ao ler tabela: {erro_leitura}"}

        return JSONResponse(dicionario_resultado)

    except Exception as erro_listagem:
        raise HTTPException(status_code=500, detail=f"Erro ao listar tabelas: {erro_listagem}")


# =====================================================================================
# ROTAS DE NEGÓCIO — CARDÁPIO
# =====================================================================================

@app.post("/cardapio/unidade/itens", tags=["cardapio"])
def ativar_itens_do_cardapio_da_unidade(
    corpo_da_requisicao_com_lista_de_ids: Dict[str, List[int]] = Body(
        ...,
        example={"itens": [1, 2, 4]},
        description=(
            "Corpo JSON contendo a lista de IDs do CARDAPIO_CENTRAL que devem "
            "ser copiados/ativados no CARDAPIO_UNIDADE. Ex.: { \"itens\": [1,2,3] }"
        ),
    ),
    gerenciador_do_banco_de_dados: SQLLiteManager = Depends(get_db),
) -> JSONResponse:
    """
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
    """
    # 1) Lê e valida o corpo
    lista_de_ids_recebidos: List[int] = corpo_da_requisicao_com_lista_de_ids.get("itens")
    if not isinstance(lista_de_ids_recebidos, list) or not all(isinstance(valor, int) for valor in lista_de_ids_recebidos):
        raise HTTPException(
            status_code=400,
            detail=(
                "O campo 'itens' deve existir e ser uma lista de números inteiros. "
                "Exemplo: { \"itens\": [1, 2, 4] }"
            )
        )

    # 2) Prepara estruturas de controle
    quantidade_de_itens_ativados: int = 0
    lista_de_erros_durante_ativacao: List[Dict[str, str]] = []

    # 3) Processa cada ID
    for id_de_um_item_do_cardapio_central in lista_de_ids_recebidos:

        # 3.1) Tenta buscar o item no CARDAPIO_CENTRAL
        try:
            registro_encontrado_no_cardapio_central = gerenciador_do_banco_de_dados.ler_registro_da_tabela_por_id(
                nome_da_tabela="CARDAPIO_CENTRAL",
                valor_id_do_registro_para_ler=id_de_um_item_do_cardapio_central
            )
        except Exception as erro_leitura:
            lista_de_erros_durante_ativacao.append({
                "id": str(id_de_um_item_do_cardapio_central),
                "erro": f"Falha ao ler CARDAPIO_CENTRAL: {erro_leitura}"
            })
            continue

        # 3.2) Se não encontrou, registra erro
        if not registro_encontrado_no_cardapio_central:
            lista_de_erros_durante_ativacao.append({
                "id": str(id_de_um_item_do_cardapio_central),
                "erro": "Item não encontrado no CARDAPIO_CENTRAL"
            })
            continue

        # 3.3) Copia para o CARDAPIO_UNIDADE
        try:
            nome_da_tabela_destino = "CARDAPIO_UNIDADE"
            colunas_para_inserir = ["COMIDA", "PRECO", "TEMPO_PREPARO"]
            valores_para_inserir = [
                registro_encontrado_no_cardapio_central["COMIDA"],
                registro_encontrado_no_cardapio_central["PRECO"],
                registro_encontrado_no_cardapio_central["TEMPO_PREPARO"],
            ]

            gerenciador_do_banco_de_dados.adicionar_registro_na_tabela(
                nome_da_tabela=nome_da_tabela_destino,
                lista_de_nomes_de_colunas=colunas_para_inserir,
                lista_de_valores_para_inserir=valores_para_inserir
            )

            quantidade_de_itens_ativados += 1

        except Exception as erro_insercao:
            lista_de_erros_durante_ativacao.append({
                "id": str(id_de_um_item_do_cardapio_central),
                "erro": f"Falha ao copiar para CARDAPIO_UNIDADE: {erro_insercao}"
            })

    # 4) Monta a resposta final
    resposta_final = {
        "quantidade_de_itens_ativados": quantidade_de_itens_ativados,
        "lista_de_erros_durante_ativacao": lista_de_erros_durante_ativacao
    }
    return JSONResponse(resposta_final)

# ===========================================
# ENDPOINT: Remover itens do cardápio da unidade por ID
# ===========================================
@app.delete("/cardapio/unidade/itens", tags=["cardapio"])
def remover_itens_do_cardapio_da_unidade(
    corpo_da_requisicao_com_lista_de_ids: Dict[str, List[int]] = Body(
        ...,
        example={"itens": [1, 3, 5]},
        description=(
            "Corpo JSON com a lista de IDs da tabela CARDAPIO_UNIDADE a serem removidos. "
            "Ex.: { \"itens\": [1,3,5] }"
        ),
    ),
    gerenciador_do_banco_de_dados: SQLLiteManager = Depends(get_db),
) -> JSONResponse:
    """
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
    curl -X DELETE http://127.0.0.1:8000/cardapio/unidade/itens \\
      -H "Content-Type: application/json" \\
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
    """
    lista_de_ids_recebidos: List[int] = corpo_da_requisicao_com_lista_de_ids.get("itens")

    if not isinstance(lista_de_ids_recebidos, list) or not all(isinstance(v, int) for v in lista_de_ids_recebidos):
        raise HTTPException(
            status_code=400,
            detail="O campo 'itens' deve existir e ser uma lista de números inteiros. Ex.: { \"itens\": [1,3,5] }"
        )

    quantidade_removidos: int = 0
    lista_de_erros: List[Dict[str, str]] = []

    for id_item_unidade in lista_de_ids_recebidos:
        try:
            gerenciador_do_banco_de_dados.remover_registro_da_tabela_por_id(
                nome_da_tabela="CARDAPIO_UNIDADE",
                valor_id_do_registro_para_remover=id_item_unidade
            )
            quantidade_removidos += 1
        except Exception as erro_remover:
            lista_de_erros.append({
                "id": str(id_item_unidade),
                "erro": f"Falha ao remover do CARDAPIO_UNIDADE: {erro_remover}"
            })

    resposta_final = {
        "quantidade_de_itens_removidos": quantidade_removidos,
        "lista_de_erros_durante_remocao": lista_de_erros
    }
    return JSONResponse(resposta_final)

# ===========================================
# ENDPOINT: Atualizar itens do cardápio da unidade por ID (parcial)
# ===========================================
@app.put("/cardapio/unidade/itens", tags=["cardapio"])
def atualizar_itens_do_cardapio_da_unidade(
    corpo_da_requisicao_com_lista_de_atualizacoes: Dict[str, List[Dict[str, Any]]] = Body(
        ...,
        example={
            "itens": [
                { "id": 3, "COMIDA": "X-BURGUER_DOBRO", "PRECO": "1900" },
                { "id": 5, "TEMPO_PREPARO": "9" }
            ]
        },
        description=(
            "Lista de atualizações parciais para registros de CARDAPIO_UNIDADE. "
            "Cada item deve ter 'id' (int) e pelo menos um campo entre: COMIDA, PRECO, TEMPO_PREPARO."
        ),
    ),
    gerenciador_do_banco_de_dados: SQLLiteManager = Depends(get_db),
) -> JSONResponse:
    """
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
    """
    lista_de_atualizacoes: List[Dict[str, Any]] = corpo_da_requisicao_com_lista_de_atualizacoes.get("itens")

    if not isinstance(lista_de_atualizacoes, list):
        raise HTTPException(status_code=400, detail="O campo 'itens' deve existir e ser uma lista com atualizações.")

    campos_permitidos = {"COMIDA", "PRECO", "TEMPO_PREPARO"}

    quantidade_atualizados: int = 0
    lista_de_erros: List[Dict[str, str]] = []
    itens_atualizados: List[Dict[str, Any]] = []

    for atualizacao in lista_de_atualizacoes:
        if not isinstance(atualizacao, dict) or "id" not in atualizacao:
            lista_de_erros.append({"erro": "Cada item deve conter 'id' e pelo menos um campo válido (COMIDA, PRECO, TEMPO_PREPARO)."})
            continue
        if not isinstance(atualizacao["id"], int):
            lista_de_erros.append({"id": str(atualizacao.get("id")), "erro": "'id' deve ser inteiro."})
            continue

        id_alvo = atualizacao["id"]

        colunas_para_alterar: List[str] = []
        valores_correspondentes: List[Any] = []

        for chave, valor in atualizacao.items():
            if chave == "id":
                continue
            if chave in campos_permitidos:
                colunas_para_alterar.append(chave)
                valores_correspondentes.append(str(valor).strip())

        if not colunas_para_alterar:
            lista_de_erros.append({
                "id": str(id_alvo),
                "erro": "Nenhum campo válido para atualizar (permitidos: COMIDA, PRECO, TEMPO_PREPARO)."
            })
            continue

        try:
            gerenciador_do_banco_de_dados.alterar_registro_da_tabela_por_id(
                nome_da_tabela="CARDAPIO_UNIDADE",
                valor_id_do_registro_para_alterar=id_alvo,
                lista_de_nomes_de_colunas_para_alterar=colunas_para_alterar,
                lista_de_novos_valores_correspondentes=valores_correspondentes
            )
            quantidade_atualizados += 1

            try:
                registro_atualizado = gerenciador_do_banco_de_dados.ler_registro_da_tabela_por_id(
                    nome_da_tabela="CARDAPIO_UNIDADE",
                    valor_id_do_registro_para_ler=id_alvo
                )
                if registro_atualizado is not None:
                    itens_atualizados.append(registro_atualizado)
                else:
                    lista_de_erros.append({
                        "id": str(id_alvo),
                        "erro": "Registro não encontrado após atualização (verifique integridade)."
                    })
            except Exception as erro_leitura_pos_update:
                lista_de_erros.append({
                    "id": str(id_alvo),
                    "erro": f"Falha ao ler registro atualizado: {erro_leitura_pos_update}"
                })

        except Exception as erro_update:
            lista_de_erros.append({
                "id": str(id_alvo),
                "erro": f"Falha ao atualizar no CARDAPIO_UNIDADE: {erro_update}"
            })

    resposta_final = {
        "quantidade_de_itens_atualizados": quantidade_atualizados,
        "lista_de_erros_durante_atualizacao": lista_de_erros,
        "itens_atualizados": itens_atualizados
    }
    return JSONResponse(resposta_final)

# ===========================================
# ENDPOINT: Inserir pedido já formatado (único) — servidor preenche HORARIO_ADICIONADO
# ===========================================
@app.post("/pedidos", tags=["pedidos"])
def adicionar_pedido_formatado_unico(
    pedido_formatado: Dict[str, Any] = Body(
        ...,
        example={
            "NUMERO_PEDIDO": "1003",
            "NOME_CLIENTE": "Carlos Mendes",
            "CPF": "11122233344",
            "COMIDAS": "HAMBURGUER, REFRIGERANTE",
            "PRECO": "2100",
            "TEMPO_PREPARO": "11"
        }
    ),
    gerenciador_do_banco_de_dados: SQLLiteManager = Depends(get_db),
) -> JSONResponse:
    """
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
    """

    # 1) Campos obrigatórios (o servidor vai preencher apenas HORARIO_ADICIONADO)
    campos_obrigatorios_sem_horario = [
        "NUMERO_PEDIDO",
        "NOME_CLIENTE",
        "CPF",
        "COMIDAS",
        "PRECO",
        "TEMPO_PREPARO",
    ]
    faltando = [c for c in campos_obrigatorios_sem_horario if c not in pedido_formatado]
    if faltando:
        raise HTTPException(
            status_code=400,
            detail=f"Campos ausentes: {', '.join(faltando)}"
        )

    # 2) Preparar valores como strings simples (fácil de entender e depurar)
    numero_pedido_str = str(pedido_formatado["NUMERO_PEDIDO"]).strip()
    nome_cliente_str = str(pedido_formatado["NOME_CLIENTE"]).strip()
    cpf_cliente_str = str(pedido_formatado["CPF"]).strip()
    comidas_str = str(pedido_formatado["COMIDAS"]).strip()
    preco_total_str = str(pedido_formatado["PRECO"]).strip()
    tempo_preparo_str = str(pedido_formatado["TEMPO_PREPARO"]).strip()

    # 3) Gerar o horário atual em epoch seconds (como string), para salvar no pedido
    horario_em_epoch_segundos_str = str(int(time.time()))

    # 4) Inserir o pedido em PEDIDOS_ATIVOS
    try:
        id_pedido_inserido = gerenciador_do_banco_de_dados.adicionar_registro_na_tabela(
            nome_da_tabela="PEDIDOS_ATIVOS",
            lista_de_nomes_de_colunas=[
                "NUMERO_PEDIDO",
                "NOME_CLIENTE",
                "CPF",
                "COMIDAS",
                "PRECO",
                "TEMPO_PREPARO",
                "HORARIO_ADICIONADO",
            ],
            lista_de_valores_para_inserir=[
                numero_pedido_str,
                nome_cliente_str,
                cpf_cliente_str,
                comidas_str,
                preco_total_str,
                tempo_preparo_str,
                horario_em_epoch_segundos_str,
            ]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Falha ao inserir pedido em PEDIDOS_ATIVOS: {e}")

    # 5) Inserir a nota fiscal em NOTAS_FISCAIS
    id_nota_inserida = None
    try:
        id_nota_inserida = gerenciador_do_banco_de_dados.adicionar_registro_na_tabela(
            nome_da_tabela="NOTAS_FISCAIS",
            lista_de_nomes_de_colunas=[
                "NUMERO_PEDIDO",
                "NOME_CLIENTE",
                "CPF",
                "PRECO"
            ],
            lista_de_valores_para_inserir=[
                numero_pedido_str,
                nome_cliente_str,
                cpf_cliente_str,
                preco_total_str
            ]
        )
    except Exception as e_nf:
        # Nota fiscal falhou, mas o pedido foi salvo. Devolvemos alerta.
        return JSONResponse({
            "mensagem": (
                "Pedido inserido com sucesso, porém houve falha ao registrar a nota fiscal. "
                "Verifique a tabela NOTAS_FISCAIS e tente registrar a nota novamente."
            ),
            "id_pedido_inserido": id_pedido_inserido,
            "erro_nota_fiscal": str(e_nf)
        }, status_code=201)

    # 6) Tudo OK: pedido + nota fiscal inseridos
    return JSONResponse({
        "mensagem": "Pedido e nota fiscal inseridos com sucesso.",
        "id_pedido_inserido": id_pedido_inserido,
        "id_nota_fiscal_inserida": id_nota_inserida
    }, status_code=201)
    

# ===========================================
# ENDPOINT: Atualizar pedidos ativos (mover prontos para histórico)
# ===========================================
@app.post("/pedidos/atualizar-status", tags=["pedidos"])
def atualizar_pedidos_ativos_movendo_para_historico(
    gerenciador_do_banco_de_dados: SQLLiteManager = Depends(get_db),
) -> JSONResponse:
    """
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
    """

    # 1) Ler todos os registros de PEDIDOS_ATIVOS
    try:
        lista_de_pedidos_ativos = gerenciador_do_banco_de_dados.ler_todos_os_registros_da_tabela("PEDIDOS_ATIVOS")
    except Exception as erro_ao_ler_ativos:
        raise HTTPException(status_code=500, detail=f"Falha ao ler PEDIDOS_ATIVOS: {erro_ao_ler_ativos}")

    # 2) Preparar estruturas de controle
    agora_em_epoch_segundos_int: int = int(time.time())
    ids_movidos_para_historico: List[int] = []
    erros_ao_processar: List[Dict[str, str]] = []
    ainda_ativos_resumo: List[Dict[str, str]] = []

    # 3) Percorrer cada pedido e decidir mover ou manter
    for pedido in lista_de_pedidos_ativos:
        # Cada 'pedido' é um dicionário com todas as colunas (inclui 'id')
        try:
            id_interno = int(pedido.get("id"))
            numero_pedido = str(pedido.get("NUMERO_PEDIDO", "")).strip()
            nome_cliente = str(pedido.get("NOME_CLIENTE", "")).strip()
            cpf_cliente = str(pedido.get("CPF", "")).strip()
            comidas = str(pedido.get("COMIDAS", "")).strip()
            preco_total = str(pedido.get("PRECO", "")).strip()
            tempo_preparo_str = str(pedido.get("TEMPO_PREPARO", "0")).strip()  # tratado como segundos
            horario_adicionado_str = str(pedido.get("HORARIO_ADICIONADO", "0")).strip()

            # Converter campos numéricos para inteiros (com proteção)
            tempo_preparo_em_segundos = int(tempo_preparo_str)
            horario_adicionado_em_segundos = int(horario_adicionado_str)

            tempo_decorrido = agora_em_epoch_segundos_int - horario_adicionado_em_segundos

            if tempo_decorrido >= tempo_preparo_em_segundos:
                # -> Este pedido está "pronto": mover para HISTORICO_PEDIDOS e remover de ATIVOS

                # 3.1) Inserir no histórico (replicando as mesmas colunas solicitadas)
                try:
                    gerenciador_do_banco_de_dados.adicionar_registro_na_tabela(
                        nome_da_tabela="HISTORICO_PEDIDOS",
                        lista_de_nomes_de_colunas=[
                            "NUMERO_PEDIDO",
                            "NOME_CLIENTE",
                            "CPF",
                            "COMIDAS",
                            "PRECO",
                            "TEMPO_PREPARO",
                            "HORARIO_ADICIONADO",
                        ],
                        lista_de_valores_para_inserir=[
                            numero_pedido,
                            nome_cliente,
                            cpf_cliente,
                            comidas,
                            preco_total,
                            str(tempo_preparo_em_segundos),     # mantemos o valor como string, coerente com o resto
                            str(horario_adicionado_em_segundos) # o mesmo horário original
                        ],
                    )
                except Exception as erro_inserir_historico:
                    erros_ao_processar.append({
                        "id": str(id_interno),
                        "erro": f"Falha ao inserir no HISTORICO_PEDIDOS: {erro_inserir_historico}"
                    })
                    # Se não conseguiu inserir no histórico, NÃO remove dos ativos
                    continue

                # 3.2) Remover dos ativos
                try:
                    gerenciador_do_banco_de_dados.remover_registro_da_tabela_por_id(
                        nome_da_tabela="PEDIDOS_ATIVOS",
                        valor_id_do_registro_para_remover=id_interno
                    )
                    ids_movidos_para_historico.append(id_interno)
                except Exception as erro_remover_ativos:
                    erros_ao_processar.append({
                        "id": str(id_interno),
                        "erro": f"Falha ao remover de PEDIDOS_ATIVOS: {erro_remover_ativos}"
                    })
                    # Obs.: Se falhar ao remover aqui, haverá item duplicado (histórico + ativo).
                    # Em POC, apenas reportamos o erro.

            else:
                # -> Ainda não está pronto; manter nos ativos e registrar um pequeno resumo
                ainda_ativos_resumo.append({
                    "id": str(id_interno),
                    "NUMERO_PEDIDO": numero_pedido,
                    "faltam_segundos": str(tempo_preparo_em_segundos - tempo_decorrido)
                })

        except Exception as erro_geral:
            erros_ao_processar.append({
                "id": str(pedido.get("id", "sem_id")),
                "erro": f"Falha ao processar pedido ativo: {erro_geral}"
            })

    # 4) Montar resposta final
    resposta = {
        "quantidade_movidos_para_historico": len(ids_movidos_para_historico),
        "ids_movidos_para_historico": ids_movidos_para_historico,
        "erros": erros_ao_processar,
        "resumo_ainda_ativos": ainda_ativos_resumo
    }
    return JSONResponse(resposta)


# =====================================================================================
# LISTAGENS INDIVIDUAIS POR TABELA
# =====================================================================================

# 1) CARDAPIO_CENTRAL -----------------------------------------------------------------
@app.get("/cardapio/central", tags=["cardapio"])
def listar_cardapio_central(
    db: SQLLiteManager = Depends(get_db)
) -> JSONResponse:
    """
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
    """
    try:
        itens = db.ler_todos_os_registros_da_tabela("CARDAPIO_CENTRAL")
        return JSONResponse(itens)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao consultar CARDAPIO_CENTRAL: {e}")


# 2) CARDAPIO_UNIDADE -----------------------------------------------------------------
@app.get("/cardapio/unidade", tags=["cardapio"])
def listar_cardapio_unidade(
    db: SQLLiteManager = Depends(get_db)
) -> JSONResponse:
    """
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
    """
    try:
        itens = db.ler_todos_os_registros_da_tabela("CARDAPIO_UNIDADE")
        return JSONResponse(itens)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao consultar CARDAPIO_UNIDADE: {e}")


# 3) PEDIDOS_ATIVOS -------------------------------------------------------------------
@app.get("/pedidos/ativos", tags=["pedidos"])
def listar_pedidos_ativos(
    db: SQLLiteManager = Depends(get_db)
) -> JSONResponse:
    """
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
    """
    try:
        itens = db.ler_todos_os_registros_da_tabela("PEDIDOS_ATIVOS")
        return JSONResponse(itens)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao consultar PEDIDOS_ATIVOS: {e}")


# 4) HISTORICO_PEDIDOS ----------------------------------------------------------------
@app.get("/pedidos/historico", tags=["pedidos"])
def listar_historico_pedidos(
    db: SQLLiteManager = Depends(get_db)
) -> JSONResponse:
    """
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
    """
    try:
        itens = db.ler_todos_os_registros_da_tabela("HISTORICO_PEDIDOS")
        return JSONResponse(itens)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao consultar HISTORICO_PEDIDOS: {e}")


# 5) NOTAS_FISCAIS --------------------------------------------------------------------
@app.get("/notas-fiscais", tags=["pedidos"])
def listar_notas_fiscais(
    db: SQLLiteManager = Depends(get_db)
) -> JSONResponse:
    """
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
    """
    try:
        itens = db.ler_todos_os_registros_da_tabela("NOTAS_FISCAIS")
        return JSONResponse(itens)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao consultar NOTAS_FISCAIS: {e}")
    



# export-openapi.py
import json
from uvicorn.importer import import_from_string

app = import_from_string("Server.BurgerFeiAPI:app")
spec = app.openapi()
with open("Server/openapi.json", "w", encoding="utf-8") as f:
    json.dump(spec, f, indent=2)