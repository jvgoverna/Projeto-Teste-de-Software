# ⚙️ Regras de Negócio — Sistema **Burguer FEI**

---

## **RN01 – Emissão automática de Nota Fiscal**

### **Descrição**
Quando um pedido é criado, o sistema gera automaticamente uma nota fiscal vinculada ao mesmo número do pedido.

### **Condições**
1. Cada nota fiscal corresponde a um único pedido (relação 1:1).

### **Entidades envolvidas**
- `PEDIDOS_ATIVOS`  
- `NOTAS_FISCAIS`

### **Resultado esperado**
A nota fiscal é criada automaticamente junto com o pedido e exibida na tela de notas fiscais.

---

## **RN02 – Ativação controlada de itens do Cardápio Central para a Unidade**

### **Descrição**
O sistema deve permitir que cada unidade **ative ou desative** itens do **cardápio central**, respeitando regras de consistência e integridade entre as tabelas de cardápio.

### **Condições**
1. Só é possível ativar itens que existam previamente no `CARDÁPIO_CENTRAL`.  
2. A ativação insere o item no `CARDÁPIO_UNIDADE`, preservando o mesmo nome, preço e tempo de preparo.  
3. Quando um item é desativado com sucesso, ele deixa de aparecer no cardápio da unidade e não pode ser incluído em novos pedidos.

### **Entidades envolvidas**
- `CARDÁPIO_CENTRAL`  
- `CARDÁPIO_UNIDADE`  

### **Resultado esperado**
A unidade só consegue ativar itens válidos da central, mantendo o cardápio sempre consistente com o estado atual do sistema.

---

## **RN03 – Movimentação automática de pedidos para o histórico com base no tempo de preparo**

### **Descrição**
O sistema deve mover automaticamente os pedidos do estado **ativo** para o **histórico** assim que o tempo de preparo estimado for atingido, garantindo atualização contínua da fila e histórico de atendimento.

### **Condições**
1. Cada pedido criado contém os campos `HORARIO_ADICIONADO` (em epoch seconds) e `TEMPO_PREPARO` (em segundos).  
2. O sistema deve comparar o tempo atual com `HORARIO_ADICIONADO + TEMPO_PREPARO` para determinar se o pedido está pronto.  
3. Se o tempo decorrido for **maior ou igual** ao tempo de preparo, o pedido deve ser:  
   - Inserido na tabela `HISTORICO_PEDIDOS`;  
   - Removido da tabela `PEDIDOS_ATIVOS`.  
5. Ao final de cada atualização, o sistema deve exibir um **resumo de status** contendo:  
   - Quantidade de pedidos movidos;  
   - IDs dos pedidos atualizados;  
   - Lista dos que ainda permanecem ativos (com o tempo restante).

### **Entidades envolvidas**
- `PEDIDOS_ATIVOS`  
- `HISTORICO_PEDIDOS`

### **Resultado esperado**
O sistema realiza automaticamente a transição de pedidos prontos para o histórico, mantendo a fila atualizada e sem perdas de dados, garantindo consistência temporal entre as tabelas.

---
