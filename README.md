# SoftFinance Backend

Um software de gerenciamento de limites de cartão de credito.

By:
- [Henrique Souza](https://github.com/NOT39) > Frontend 
- [Davi Lucciola](https://github.com/NOT39) > Backend

## Backend

### MicroServiços

O backend foi dividido em três serviços principais:

1. Serviço de Autenticação
- Será responsavel pelo cadastro de usuarios na plataforma e controle de autenticação
- Só poderá ter um usuario logado por vez na plataforma

2. Serviço do Cliente
- Será responsavel pelo gerenciamento de recursos do cliente.

3. Serviço de Transação
- Será responsavel pelo registro de qualquer transação realizada pelo cliente
- Aqui também terá as consultas com filtro de categoria

### Como rodar localmente:

- Rode o comando:
> `docker-compose -up -d`

**OBS: ainda não está funcionando**