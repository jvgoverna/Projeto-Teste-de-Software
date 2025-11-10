from src.services.realizar_pedido_service import RealizarPedidoService
from src.services.pedidos_fila_service import PedidosFilaService
from src.services.visualizar_historico_service import HistoricoService
from src.services.visualizar_notas_fiscais_service import VisualizarNotasFiscaisService
from src.services.editar_itens_cardapio_service import EditarItensCardapioService

service_realizar_pedido = RealizarPedidoService()
service_pedidos_fila = PedidosFilaService()
service_historico = HistoricoService()
service_notas_fiscais = VisualizarNotasFiscaisService()
service_editar_itens = EditarItensCardapioService()

def test_criar_pedido_mostrar_fila_preparo():

    resp_realizar_pedido = service_realizar_pedido.criar_pedido( 
        numero_pedido="9999",
        nome_cliente="TESTANDO INTEGRACAO",
        cpf="11122233344",
        comidas=["HAMBURGUER"],
        preco_total_reais=15.00,
        tempo_preparo_total_min="10"
    )

    assert isinstance(resp_realizar_pedido, dict)

    pedidos_ativos = service_pedidos_fila.listar_pedidos_ativos()

    # verifica se o pedido criado está na lista
    numeros = [p["NUMERO_PEDIDO"] for p in pedidos_ativos]
    assert "9999" in numeros


def test_criar_pedido_com_numero_pedido_duplicado():
    numero = "6666"

    # cria o pedido pela primeira vez
    resp_realizar_pedido1 = service_realizar_pedido.criar_pedido( 
        numero_pedido=numero,
        nome_cliente="TESTANDO INTEGRACAO COM NUMERO PEDIDO DUPLICADO",
        cpf="11122233344",
        comidas=["HAMBURGUER"],
        preco_total_reais=15.00,
        tempo_preparo_total_min=10,
    )
    assert isinstance(resp_realizar_pedido1, dict)
    
    # cria o mesmo pedido de novo
    resp_realizar_pedido2 = service_realizar_pedido.criar_pedido( 
        numero_pedido=numero,
        nome_cliente="TESTANDO INTEGRACAO COM NUMERO PEDIDO DUPLICADO",
        cpf="11122233344",
        comidas=["HAMBURGUER"],
        preco_total_reais=15.00,
        tempo_preparo_total_min=10,
    )
    assert isinstance(resp_realizar_pedido2, dict)

    # verifica na fila quantas vezes o 6666 apareceu
    pedidos_ativos = service_pedidos_fila.listar_pedidos_ativos()
    numeros = [p["NUMERO_PEDIDO"] for p in pedidos_ativos]

    assert numeros.count(numero) >= 2   # o sistema deixou duplicar

def test_criar_pedido_com_comidas_vazias():
    numero = "7777"

    resp_realizar_pedido1 = service_realizar_pedido.criar_pedido( 
        numero_pedido=numero,
        nome_cliente="TESTANDO INTEGRACAO COM COMIDAS VAZIO",
        cpf="11122233344",
        comidas=[],
        preco_total_reais=15.00,
        tempo_preparo_total_min=10,
    )
    assert isinstance(resp_realizar_pedido1, dict)
    
    resp_realizar_pedido2 = service_realizar_pedido.criar_pedido( 
        numero_pedido=numero,
        nome_cliente="TESTANDO INTEGRACAO COM COMIDAS VAZIO",
        cpf="11122233344",
        comidas=[],
        preco_total_reais=15.00,
        tempo_preparo_total_min=10,
    )
    assert isinstance(resp_realizar_pedido2, dict)

    pedidos_ativos = service_pedidos_fila.listar_pedidos_ativos()
    numeros = [p["NUMERO_PEDIDO"] for p in pedidos_ativos]

    assert numeros.count(numero) >= 2

def test_listar_historico_pedidos_notas_fiscais():

    historico_pedido = service_historico.listar_historico()
    notas_fiscais = service_notas_fiscais.listar_notas_fiscais()

    for item in historico_pedido:
        if item in notas_fiscais:
            assert "9999" in item['NUMERO_PEDIDO']
            assert "TESTANDO INTEGRACAO" in item["NOME_CLIENTE"]
            assert "11122233344" in item["CPF"]
            assert "1500" in item["PRECO"]

def test_ativar_todos_itens_cardapio_unidade():
    cardapio_unidade = service_editar_itens.listar_cardapio_unidade()
    cardapio_central = service_editar_itens.listar_cardapio_central()


    assert len(cardapio_central) > 0

    # Conjunto de comidas já ativas na unidade
    comidas_unidade = {item["COMIDA"] for item in cardapio_unidade}
    
    # Conjunto de comidas disponíveis no cardápio central
    comidas_central = {item["COMIDA"] for item in cardapio_central}

    # Quais comidas do central ainda NÃO estão na unidade?
    comidas_para_ativar = [c for c in comidas_central if c not in comidas_unidade]

    # não tem nada novo pra ativar
    if not comidas_para_ativar:

        assert comidas_central.issubset(comidas_unidade)
        return  # não chama o serviço, evita mandar lista vazia

    # tem coisas novas pra ativar
    # Descobre os IDs no cardápio central correspondentes às comidas que faltam
    ids_ativacao = [
        item["id"]
        for item in cardapio_central
        if item["COMIDA"] in comidas_para_ativar
    ]


    assert ids_ativacao, "Não foram encontrados IDs para ativação"


    service_editar_itens.ativar_itens_cardapio_unidade(ids_ativacao)


    cardapio_unidade_atualizado = service_editar_itens.listar_cardapio_unidade()
    comidas_unidade_atualizado = {item["COMIDA"] for item in cardapio_unidade_atualizado}

    # Verifica se todas as comidas que faltavam agora estão presentes
    for comida in comidas_para_ativar:
        assert comida in comidas_unidade_atualizado


def test_remover_todos_itens_cardapio_unidade():
    cardapio_unidade = service_editar_itens.listar_cardapio_unidade()

    comidas_cardapio_unidade = []
    for item in cardapio_unidade:
        comidas_cardapio_unidade.append(item['COMIDA'])

    ids_remocao = []
    for item in cardapio_unidade:
        ids_remocao.append(item['id'])

    
    service_editar_itens.remover_itens_cardapio_unidade(ids_remocao)

    cardapio_unidade_atualizado = service_editar_itens.listar_cardapio_unidade()

    comidas_atuais = []
    for item in cardapio_unidade_atualizado:
        comidas_atuais.append(item['COMIDA'])

    for comida in comidas_atuais:
        assert comida not in comidas_atuais

def test_ativar_itens_repetidos_cardapio_unidade():
    cardapio_central = service_editar_itens.listar_cardapio_central()

    item_central = cardapio_central[0]
    id_item = item_central['id']

    service_editar_itens.ativar_itens_cardapio_unidade([id_item])
    service_editar_itens.ativar_itens_cardapio_unidade([id_item])

    cardapio_unidade_atualizado= service_editar_itens.listar_cardapio_unidade()

    comidas_ativas = []
    for item in cardapio_unidade_atualizado:
        comidas_ativas.append(item['COMIDA'])
    
    assert item_central["COMIDA"] in comidas_ativas

def test_remover_comida_especifica_cardapio_unidade():
    cardapio_unidade = service_editar_itens.listar_cardapio_unidade()

    ids_remocao = []
    for item in cardapio_unidade:
        if item['COMIDA'] == "HAMBURGUER":
            ids_remocao.append(item['id'])
    
    service_editar_itens.remover_itens_cardapio_unidade(ids_remocao)

    cardapio_atualizado = service_editar_itens.listar_cardapio_unidade()

    comidas_cardapio_atualizado = []
    for item in cardapio_atualizado:
        comidas_cardapio_atualizado.append(item['COMIDA'])

    for comida in comidas_cardapio_atualizado:
        assert comida not in comidas_cardapio_atualizado
    
def test_listar_historico():
    historico = service_historico.listar_historico()

    assert isinstance(historico, list)

    if historico:
        for item in historico:
            assert "NUMERO_PEDIDO" in item
            assert "NOME_CLIENTE" in item
            assert "CPF" in item
            assert "COMIDAS" in item
            assert "PRECO" in item
            assert "TEMPO_PREPARO" in item
            assert "HORARIO_ADICIONADO" in item

def test_listar_notas_fiscais():
    notas_fiscais = service_notas_fiscais.listar_notas_fiscais()

    assert isinstance(notas_fiscais, list)

    if notas_fiscais:
        for item in notas_fiscais:
            assert "NUMERO_PEDIDO" in item
            assert "NOME_CLIENTE" in item
            assert "CPF" in item
            assert "PRECO" in item
