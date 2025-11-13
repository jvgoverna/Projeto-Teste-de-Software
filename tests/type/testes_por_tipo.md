# Casos de Teste – Burguer FEI (REST + Mock)

## Como executar os testes

### 1. Instalar dependências do projeto

No diretório raiz do projeto:

    pip install -r src/requirements.txt

*(ajuste o comando se seu projeto usar outro gerenciador ou arquivo de dependências)*

---

### 2. Subir o servidor FastAPI (necessário para os testes REST)

Em um terminal, entrar na pastas scr/ e subir o servidor na porta `8000`:

    uvicorn Server.BurgerFeiAPI:app --reload --port 8000

> Deixe esse terminal aberto enquanto executa os testes de API (`test_api_rest.py`), pois eles chamam o servidor real via HTTP.

---

### 3. Rodar os testes REST (API real)

Em outro terminal, executar:

    pytest tests/type/test_api_rest.py -v

---

### 4. Rodar os testes com mock/stub (não exigem servidor ativo)

Estes testes usam `TestClient` e mocks, então não precisam do `uvicorn` rodando:

    pytest tests/type/test_mock_stub.py -v

---

## 📋 Casos de Teste – Resumo

| **CT** | **Ação / Cenário Testado** |
|--------|------------------------------|
| **CT01** | Enviar GET `/health` e validar resposta 200 com `{"status": "ok"}`. |
| **CT02** | Enviar GET `/cardapio/central` e verificar lista com campos `COMIDA`, `PRECO`, `TEMPO_PREPARO`. |
| **CT03** | Enviar POST `/pedidos` com payload completo e validar criação (201) + IDs retornados. |
| **CT04** | Ativar item da central via POST `/cardapio/unidade/itens` e verificar listagem da unidade via GET `/cardapio/unidade`. |
| **CT05** | Enviar POST `/cardapio/unidade/itens` com tipos inválidos e validar erro 422. |
| **CT06** | Ativar item da unidade e depois remover via DELETE `/cardapio/unidade/itens`. |
| **CT07** | Mockar DB e enviar GET `/db/ping`, validando retorno `"db": "connected"`. |
| **CT08** | Simular erro no DB via mock e enviar GET `/db/ping`, esperando 500 com mensagem de falha. |
| **CT09** | Mockar retorno de lista e validar GET `/cardapio/unidade` retornando exatamente os itens do mock. |
| **CT10** | Simular exceção no mock ao listar unidade e validar retorno HTTP 500. |
| **CT11** | Enviar DELETE `/cardapio/unidade/itens` com IDs válidos no mock e validar remoção total. |
| **CT12** | Simular falha ao remover um dos IDs no mock e validar remoção parcial + erro registrado. |


## Resumo Geral da Execução dos Testes por tipo:

Todos os testes foram executados com sucesso, abrangendo tanto a API real (via chamadas HTTP) quanto os testes isolados com mock/stub.  
As funcionalidades principais — cardápio central, cardápio da unidade, criação de pedidos, interação com banco de dados e remoção de itens — responderam exatamente conforme esperado.

- O servidor FastAPI operou de forma estável durante toda a suíte de testes.
- Os endpoints REST retornaram os códigos HTTP corretos e estruturas de dados válidas.
- As validações do FastAPI/Pydantic funcionaram conforme o esperado, rejeitando entradas inválidas.
- O comportamento do banco de dados mockado demonstrou que o sistema trata exceções de maneira segura e previsível.
- Fluxos completos, como criação de pedidos e ativação/remoção de itens do cardápio, apresentaram funcionamento consistente.
