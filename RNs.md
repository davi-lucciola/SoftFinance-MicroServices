# Entidades e Regras

# Apis

## Api Auth (Usuario e Login)

### Usuario

- id
- email
- senha

### Token

- id
- data_criacao
- data_expiracao
- usuario_id
- token_de_acesso

## Api Cliente (Recursos do Cliente)

### Cartao

- id
- limite
- gasto_total -> soma das operacoes do usuario
- usuario_id (Foreing Key)

### Categoria

- id
- cor
- icone
- nome_categoria
- usuario_id (Foreing Key)

> usuario_id = null -> categoria do sistema

### Api Transação (Transações)

## Operação

- id
- usuario_id (Foreing Key)
- data_operacao
- valor_total
- tipo -> Enum: ['Crédito', ]
- status -> Enum ['FINALIZADA', 'EM_ANDAMENTO']
- categoria_id (Foreing Key)

# Pagamento

- id
- operacao_id
- parcelas_pagas
- parcelas_totais
- valor

## Fatura

- id
- data_inicio
- data_fechamento
- data_vencimento
- usuario_id
- valor_total
- status_pagamento -> Enum Status: ['ABERTA', 'FECHADA', 'VENCIDA']