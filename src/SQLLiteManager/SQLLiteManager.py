# arquivo: SQLLiteManager.py
"""
Gerenciador genérico para SQLite, com operações básicas de CRUD.

Este módulo fornece a classe `SQLLiteManager`, que encapsula:
- Abertura/fechamento de conexão com um arquivo SQLite.
- Criação de tabela genérica (nome, colunas e tipos).
- Inserção, leitura (por ID e de todos), atualização e remoção de registros.

PRÉ-REQUISITOS
--------------
- Python 3.9+ (recomendado)
- Nenhuma dependência externa além da biblioteca padrão (sqlite3, re)

EXEMPLO RÁPIDO
--------------
    gerenciador = SQLLiteManager("lanchonete.db")
    gerenciador.abrir_conexao_com_banco_sqlite()
    gerenciador.criar_tabela_generica(
        nome_da_tabela="cardapio",
        lista_de_nomes_de_colunas=["Comida", "Preco", "TempoPreparo"],
        lista_de_tipos_de_colunas=["TEXT", "TEXT", "TEXT"]
    )
    novo_id = gerenciador.adicionar_registro_na_tabela(
        "cardapio",
        ["Comida", "Preco", "TempoPreparo"],
        ["X-Burger", "1500", "10"]
    )
    item = gerenciador.ler_registro_da_tabela_por_id("cardapio", novo_id)
    todos = gerenciador.ler_todos_os_registros_da_tabela("cardapio")
    gerenciador.alterar_registro_da_tabela_por_id("cardapio", novo_id, ["Preco"], ["1800"])
    gerenciador.remover_registro_da_tabela_por_id("cardapio", novo_id)
    gerenciador.fechar_conexao_com_banco_sqlite()
"""

import sqlite3
import re
from typing import Any, Dict, List, Optional, Sequence

db_path = "/Database"

class SQLLiteManager:
    """Gerencia um banco SQLite com operações genéricas, de forma clara para iniciantes.

    Esta classe evita "mágicas" e usa apenas a biblioteca padrão. Os nomes dos métodos
    são descritivos e cada método realiza uma única responsabilidade (criar tabela,
    inserir, ler, atualizar, remover).

    Atributos:
        caminho_completo_arquivo_banco_sqlite (str): Caminho do arquivo .db no disco.
        conexao_ativa_banco_sqlite (sqlite3.Connection | None): Conexão ativa (ou None).
    """

    def __init__(self, caminho_completo_arquivo_banco_sqlite: str = db_path) -> None:
        """Inicializa o gerenciador com o caminho do arquivo SQLite.

        Args:
            caminho_completo_arquivo_banco_sqlite: Caminho completo do arquivo .db.
        """
        self.caminho_completo_arquivo_banco_sqlite: str = caminho_completo_arquivo_banco_sqlite
        self.conexao_ativa_banco_sqlite: Optional[sqlite3.Connection] = None

    # =========================================================
    # SEÇÃO 1 — CONEXÃO
    # =========================================================
    def abrir_conexao_com_banco_sqlite(self) -> None:
        """Abre a conexão com o banco SQLite.

        Se já houver uma conexão aberta, não faz nada.

        Raises:
            sqlite3.Error: Se ocorrer falha ao abrir o arquivo de banco.
        """
        if self.conexao_ativa_banco_sqlite is not None:
            # Já existe uma conexão aberta; não reabrir.
            return
        self.conexao_ativa_banco_sqlite = sqlite3.connect(
            self.caminho_completo_arquivo_banco_sqlite,
            check_same_thread=False
            )
        print("[OK] Conexão aberta com o banco:", self.caminho_completo_arquivo_banco_sqlite)

    def fechar_conexao_com_banco_sqlite(self) -> None:
        """Fecha a conexão ativa com o banco, se existir.

        Esta operação é idempotente (pode ser chamada várias vezes sem erro).
        """
        if self.conexao_ativa_banco_sqlite is not None:
            self.conexao_ativa_banco_sqlite.close()
            self.conexao_ativa_banco_sqlite = None
            print("[OK] Conexão fechada com o banco.")

    # =========================================================
    # SEÇÃO 2 — VALIDAÇÕES SIMPLES (SEGURANÇA BÁSICA)
    # =========================================================
    def validar_nome_identificador_simples(self, nome_identificador_para_validar: Any) -> bool:
        """Valida nomes de tabela/coluna (apenas letras, números e underscore).

        Em SQLite (e SQL em geral), **placeholders (?)** só funcionam para valores,
        não para identificadores (nomes de tabela/coluna). Por isso validamos os nomes
        manualmente para reduzir risco de erros e injeções.

        Args:
            nome_identificador_para_validar: Texto do nome a validar.

        Returns:
            True se o nome for válido; False caso contrário.
        """
        if not isinstance(nome_identificador_para_validar, str):
            return False
        padrao = r"^[A-Za-z0-9_]+$"
        return re.fullmatch(padrao, nome_identificador_para_validar) is not None

    def validar_lista_de_nomes_identificadores(self, lista_de_nomes_para_validar: Any) -> bool:
        """Valida uma lista/tupla de nomes de identificadores.

        Args:
            lista_de_nomes_para_validar: Lista ou tupla com nomes de colunas/tabelas.

        Returns:
            True se todos os nomes forem válidos; False caso contrário.
        """
        if not isinstance(lista_de_nomes_para_validar, (list, tuple)):
            return False
        for nome_unico in lista_de_nomes_para_validar:
            if not self.validar_nome_identificador_simples(nome_unico):
                return False
        return True

    # =========================================================
    # SEÇÃO 3 — CRIAR TABELA GENÉRICA
    # =========================================================
    def criar_tabela_generica(
        self,
        nome_da_tabela: str,
        lista_de_nomes_de_colunas: Sequence[str],
        lista_de_tipos_de_colunas: Sequence[str],
    ) -> None:
        """Cria uma tabela com `id` autoincremento e colunas definidas pelo usuário.

        A coluna `id` é sempre criada como:
            `id INTEGER PRIMARY KEY AUTOINCREMENT`

        Args:
            nome_da_tabela: Nome da tabela (somente A–Z, a–z, 0–9 e _).
            lista_de_nomes_de_colunas: Lista com os nomes das colunas (ex.: ["Comida","Preco","TempoPreparo"]).
            lista_de_tipos_de_colunas: Lista com os tipos das colunas (ex.: ["TEXT","TEXT","TEXT"]).

        Raises:
            ValueError: Se nomes ou listas forem inválidos/inconsistentes.
            sqlite3.Error: Se o comando SQL falhar por algum motivo.

        Example:
            >>> gerenciador.criar_tabela_generica(
            ...     "cardapio",
            ...     ["Comida", "Preco", "TempoPreparo"],
            ...     ["TEXT", "TEXT", "TEXT"]
            ... )
        """
        # Validações básicas de segurança e coerência
        if not self.validar_nome_identificador_simples(nome_da_tabela):
            raise ValueError("Nome da tabela inválido. Use apenas letras, números e underscore.")
        if not self.validar_lista_de_nomes_identificadores(lista_de_nomes_de_colunas):
            raise ValueError("Há nomes de colunas inválidos. Use apenas letras, números e underscore.")
        if (not isinstance(lista_de_tipos_de_colunas, (list, tuple))
                or len(lista_de_nomes_de_colunas) != len(lista_de_tipos_de_colunas)):
            raise ValueError("As listas de colunas e tipos devem existir e ter o MESMO tamanho.")

        # Monta o trecho "Comida TEXT, Preco TEXT, TempoPreparo TEXT"
        partes_definicao_colunas_sql: List[str] = []
        for indice in range(len(lista_de_nomes_de_colunas)):
            nome_coluna_atual = lista_de_nomes_de_colunas[indice]
            tipo_coluna_atual = lista_de_tipos_de_colunas[indice]
            partes_definicao_colunas_sql.append(f"{nome_coluna_atual} {tipo_coluna_atual}")

        texto_sql_definicao_colunas = ", ".join(partes_definicao_colunas_sql)

        # Cria a tabela com id autoincremento e as colunas definidas
        texto_sql_criacao_tabela = f"""
        CREATE TABLE IF NOT EXISTS {nome_da_tabela} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {texto_sql_definicao_colunas}
        );
        """

        self.conexao_ativa_banco_sqlite.execute(texto_sql_criacao_tabela)
        self.conexao_ativa_banco_sqlite.commit()
        print(f"[OK] Tabela '{nome_da_tabela}' criada (ou já existia).")

    # =========================================================
    # SEÇÃO 4 — INSERIR REGISTRO
    # =========================================================
    def adicionar_registro_na_tabela(
        self,
        nome_da_tabela: str,
        lista_de_nomes_de_colunas: Sequence[str],
        lista_de_valores_para_inserir: Sequence[Any],
    ) -> int:
        """Insere um registro na tabela informada.

        Args:
            nome_da_tabela: Nome da tabela onde inserir (ex.: "cardapio").
            lista_de_nomes_de_colunas: Colunas alvo (ex.: ["Comida","Preco","TempoPreparo"]).
            lista_de_valores_para_inserir: Valores na MESMA ordem das colunas (ex.: ["X-Burger","1500","10"]).

        Returns:
            O `id` (int) gerado para o novo registro.

        Raises:
            ValueError: Se nomes/quantidades forem inválidos.
            sqlite3.Error: Se a inserção falhar no SQLite.

        Observação:
            Usa placeholders (?) para valores (seguro) e valida nomes de colunas/tabela.
        """
        if not self.validar_nome_identificador_simples(nome_da_tabela):
            raise ValueError("Nome da tabela inválido.")
        if not self.validar_lista_de_nomes_identificadores(lista_de_nomes_de_colunas):
            raise ValueError("Há nomes de colunas inválidos.")
        if (not isinstance(lista_de_valores_para_inserir, (list, tuple))
                or len(lista_de_nomes_de_colunas) != len(lista_de_valores_para_inserir)):
            raise ValueError("Listas de colunas e valores devem ter o MESMO tamanho.")

        # Monta "Comida, Preco, TempoPreparo"
        texto_sql_lista_colunas = ", ".join(lista_de_nomes_de_colunas)
        # Monta "?, ?, ?"
        texto_sql_placeholders = ", ".join(["?"] * len(lista_de_valores_para_inserir))

        texto_sql_insert_generico = (
            f"INSERT INTO {nome_da_tabela} ({texto_sql_lista_colunas}) "
            f"VALUES ({texto_sql_placeholders})"
        )

        try:
            self.conexao_ativa_banco_sqlite.execute("BEGIN")
            self.conexao_ativa_banco_sqlite.execute(texto_sql_insert_generico, tuple(lista_de_valores_para_inserir))
            self.conexao_ativa_banco_sqlite.commit()
            novo_id_gerado = self.conexao_ativa_banco_sqlite.execute(
                "SELECT last_insert_rowid()"
            ).fetchone()[0]
            print(f"[OK] Registro inserido em '{nome_da_tabela}' com id={novo_id_gerado}.")
            return int(novo_id_gerado)
        except Exception as erro:
            self.conexao_ativa_banco_sqlite.rollback()
            print("[ERRO] Falha ao inserir registro:", erro)
            raise erro

    # =========================================================
    # SEÇÃO 5 — REMOVER REGISTRO
    # =========================================================
    def remover_registro_da_tabela_por_id(self, nome_da_tabela: str, valor_id_do_registro_para_remover: int) -> None:
        """Remove um registro da tabela usando o `id`.

        Args:
            nome_da_tabela: Nome da tabela (ex.: "cardapio").
            valor_id_do_registro_para_remover: Valor inteiro do `id` a remover.

        Raises:
            ValueError: Se o nome da tabela for inválido.
            sqlite3.Error: Se o comando SQL falhar.

        Observação:
            Se o `id` não existir, nenhuma linha será afetada (sem erro).
        """
        if not self.validar_nome_identificador_simples(nome_da_tabela):
            raise ValueError("Nome da tabela inválido.")

        try:
            self.conexao_ativa_banco_sqlite.execute("BEGIN")
            self.conexao_ativa_banco_sqlite.execute(
                f"DELETE FROM {nome_da_tabela} WHERE id = ?",
                (valor_id_do_registro_para_remover,)
            )
            self.conexao_ativa_banco_sqlite.commit()
            print(f"[OK] Registro id={valor_id_do_registro_para_remover} removido de '{nome_da_tabela}'.")
        except Exception as erro:
            self.conexao_ativa_banco_sqlite.rollback()
            print("[ERRO] Falha ao remover registro:", erro)
            raise erro

    # =========================================================
    # SEÇÃO 6 — ATUALIZAR REGISTRO
    # =========================================================
    def alterar_registro_da_tabela_por_id(
        self,
        nome_da_tabela: str,
        valor_id_do_registro_para_alterar: int,
        lista_de_nomes_de_colunas_para_alterar: Sequence[str],
        lista_de_novos_valores_correspondentes: Sequence[Any],
    ) -> None:
        """Atualiza colunas específicas de um registro identificado por `id`.

        Args:
            nome_da_tabela: Nome da tabela (ex.: "cardapio").
            valor_id_do_registro_para_alterar: ID do registro que será atualizado.
            lista_de_nomes_de_colunas_para_alterar: Colunas a atualizar (ex.: ["Comida","Preco"]).
            lista_de_novos_valores_correspondentes: Novos valores na mesma ordem (ex.: ["X-Burger Duplo","1800"]).

        Raises:
            ValueError: Se os nomes forem inválidos ou listas tiverem tamanhos diferentes.
            sqlite3.Error: Se o comando SQL falhar.

        Observações:
            Se o `id` não existir, nenhuma linha será afetada (sem erro).
        """
        if not self.validar_nome_identificador_simples(nome_da_tabela):
            raise ValueError("Nome da tabela inválido.")
        if not self.validar_lista_de_nomes_identificadores(lista_de_nomes_de_colunas_para_alterar):
            raise ValueError("Há nomes de colunas inválidos.")
        if (not isinstance(lista_de_novos_valores_correspondentes, (list, tuple))
                or len(lista_de_nomes_de_colunas_para_alterar) != len(lista_de_novos_valores_correspondentes)):
            raise ValueError("Listas de colunas e valores devem ter o MESMO tamanho.")

        # Monta "Comida = ?, Preco = ?"
        lista_de_atribuicoes_para_update: List[str] = []
        for nome_coluna in lista_de_nomes_de_colunas_para_alterar:
            lista_de_atribuicoes_para_update.append(f"{nome_coluna} = ?")
        texto_sql_atribuicoes = ", ".join(lista_de_atribuicoes_para_update)

        texto_sql_update_generico = f"UPDATE {nome_da_tabela} SET {texto_sql_atribuicoes} WHERE id = ?"

        try:
            self.conexao_ativa_banco_sqlite.execute("BEGIN")
            self.conexao_ativa_banco_sqlite.execute(
                texto_sql_update_generico,
                tuple(lista_de_novos_valores_correspondentes) + (valor_id_do_registro_para_alterar,)
            )
            self.conexao_ativa_banco_sqlite.commit()
            print(f"[OK] Registro id={valor_id_do_registro_para_alterar} atualizado em '{nome_da_tabela}'.")
        except Exception as erro:
            self.conexao_ativa_banco_sqlite.rollback()
            print("[ERRO] Falha ao atualizar registro:", erro)
            raise erro

    # =========================================================
    # SEÇÃO 7 — LER REGISTRO POR ID
    # =========================================================
    def ler_registro_da_tabela_por_id(self, nome_da_tabela: str, valor_id_do_registro_para_ler: int) -> Optional[Dict[str, Any]]:
        """Lê um registro específico da tabela e retorna um dicionário `{coluna: valor}`.

        Args:
            nome_da_tabela: Nome da tabela (ex.: "cardapio").
            valor_id_do_registro_para_ler: ID do registro a ser lido.

        Returns:
            Um dicionário com todas as colunas (incluindo `id`) e seus valores;
            ou `None` se não houver registro com esse ID.

        Raises:
            ValueError: Se o nome da tabela for inválido.
            sqlite3.Error: Se a consulta falhar.
        """
        if not self.validar_nome_identificador_simples(nome_da_tabela):
            raise ValueError("Nome da tabela inválido.")

        cursor_consulta = self.conexao_ativa_banco_sqlite.execute(
            f"SELECT * FROM {nome_da_tabela} WHERE id = ?",
            (valor_id_do_registro_para_ler,)
        )
        descricao_das_colunas = [descricao[0] for descricao in cursor_consulta.description]
        linha_lida = cursor_consulta.fetchone()

        if linha_lida is None:
            return None

        dicionario_resultado: Dict[str, Any] = {}
        for indice_coluna, nome_coluna in enumerate(descricao_das_colunas):
            dicionario_resultado[nome_coluna] = linha_lida[indice_coluna]
        return dicionario_resultado

    # =========================================================
    # SEÇÃO 8 — LER TODOS OS REGISTROS
    # =========================================================
    def ler_todos_os_registros_da_tabela(self, nome_da_tabela: str) -> List[Dict[str, Any]]:
        """Lê todos os registros de uma tabela e retorna uma lista de dicionários.

        Args:
            nome_da_tabela: Nome da tabela (ex.: "cardapio").

        Returns:
            Uma lista de dicionários, onde cada dicionário representa um registro
            com `{coluna: valor}` (inclui a coluna `id`). Se a tabela estiver vazia,
            retorna `[]`.

        Raises:
            ValueError: Se o nome da tabela for inválido.
            sqlite3.Error: Se a consulta falhar.
        """
        if not self.validar_nome_identificador_simples(nome_da_tabela):
            raise ValueError("Nome da tabela inválido.")

        cursor_consulta = self.conexao_ativa_banco_sqlite.execute(f"SELECT * FROM {nome_da_tabela}")
        descricao_das_colunas = [descricao[0] for descricao in cursor_consulta.description]
        lista_com_todos_os_registros: List[Dict[str, Any]] = []

        linhas_encontradas = cursor_consulta.fetchall()
        for linha_unica in linhas_encontradas:
            dicionario_registro: Dict[str, Any] = {}
            for indice_coluna, nome_coluna in enumerate(descricao_das_colunas):
                dicionario_registro[nome_coluna] = linha_unica[indice_coluna]
            lista_com_todos_os_registros.append(dicionario_registro)

        return lista_com_todos_os_registros


# =============================================================
# EXEMPLO DE USO — TEMA LANCHONETE (cardápio)
# =============================================================
if __name__ == "__main__":
    # 1) Criar gerenciador e abrir conexão
    gerenciador = SQLLiteManager("lanchonete.db")
    gerenciador.abrir_conexao_com_banco_sqlite()

    # 2) Criar tabela do cardápio com 3 colunas de texto
    nome_da_tabela_cardapio = "cardapio"
    lista_colunas_cardapio = ["Comida", "Preco", "TempoPreparo"]
    lista_tipos_cardapio = ["TEXT", "TEXT", "TEXT"]
    gerenciador.criar_tabela_generica(
        nome_da_tabela=nome_da_tabela_cardapio,
        lista_de_nomes_de_colunas=lista_colunas_cardapio,
        lista_de_tipos_de_colunas=lista_tipos_cardapio
    )

    # 3) Inserir alguns itens no cardápio
    id_x_burger = gerenciador.adicionar_registro_na_tabela(
        nome_da_tabela=nome_da_tabela_cardapio,
        lista_de_nomes_de_colunas=lista_colunas_cardapio,
        lista_de_valores_para_inserir=["X-Burger", "1500", "10"]
    )
    id_batata = gerenciador.adicionar_registro_na_tabela(
        nome_da_tabela=nome_da_tabela_cardapio,
        lista_de_nomes_de_colunas=lista_colunas_cardapio,
        lista_de_valores_para_inserir=["Batata Frita", "850", "5"]
    )
    id_refri = gerenciador.adicionar_registro_na_tabela(
        nome_da_tabela=nome_da_tabela_cardapio,
        lista_de_nomes_de_colunas=lista_colunas_cardapio,
        lista_de_valores_para_inserir=["Refrigerante", "600", "1"]
    )

    # 4) Ler um item por ID
    print("\nItem específico (ID X-Burger):")
    print(gerenciador.ler_registro_da_tabela_por_id(nome_da_tabela_cardapio, id_x_burger))

    # 5) Ler todos os itens
    print("\nCardápio completo (todos os registros):")
    for registro in gerenciador.ler_todos_os_registros_da_tabela(nome_da_tabela_cardapio):
        print(registro)

    # 6) Alterar um item (mudar nome e preço do X-Burger)
    gerenciador.alterar_registro_da_tabela_por_id(
        nome_da_tabela=nome_da_tabela_cardapio,
        valor_id_do_registro_para_alterar=id_x_burger,
        lista_de_nomes_de_colunas_para_alterar=["Comida", "Preco"],
        lista_de_novos_valores_correspondentes=["X-Burger Duplo", "1800"]
    )

    # 7) Remover um item (ex.: Refrigerante)
    gerenciador.remover_registro_da_tabela_por_id(nome_da_tabela_cardapio, id_refri)

    # 8) Ler todos novamente (estado final)
    print("\nCardápio após alterações:")
    for registro in gerenciador.ler_todos_os_registros_da_tabela(nome_da_tabela_cardapio):
        print(registro)

    # 9) Fechar conexão
    gerenciador.fechar_conexao_com_banco_sqlite()