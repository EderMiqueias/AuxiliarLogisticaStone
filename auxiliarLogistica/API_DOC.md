# Sobre o desenvolvimento da API

A API foi desenvolvida usando o [falcon framework](https://falconframework.org/).
A mesma usa como base inicial de dados os arquivos csv disponibilizados junto com a descrição do
projeto, e faz uma migração destes dados para um db [sqlite](https://www.sqlite.org/index.html) que é a forma principal
de armazenamento de dados desta aplicação.



# Sobre o funcionamento da API

## Requisições e respostas

Os metodos de requisições aceitas pela API são GET e POST. Todas as respostas da API são enviadas no formato JSON.
Definidos nas seguintes rotas:

## /
#### GET
Retorna uma simples mensagem de boas vindas a API, o proposito é indicar que a mesma está operando perfeitamente.

#### POST
Metodo não é aceito e "Dropa" a requisição.


## /polos
#### GET
Retorna uma lista de objetos JSON com as informações necessárias de todos os polos cadastrados.
Um exemplo de objeto retornado na lista:

```json
{
    "id": 39,
    "base": "PB - PATOS",
    "estoque": 130,
    "url": "pb-patos",
    "average": 3.5035971223021583
}
```

id -> Identificados do polo no banco de dados.
base -> Sigla do estado e municipio onde o polo está localizado.
estoque -> Quantidade de terminais disponiveis no estoque deste polo.
url -> É o atributo base emm lowercase sem espaços para servir de identificado de url para requisições POST.
average -> Baseado na base de dados dos atendimentos, a api gera a média de consumo diário daquele polo.

#### POST
Metodo não é aceito e "Dropa" a requisição.


## /polos/{polo-url}
#### GET

Retorna um objeto JSON único semelhante ao exemplo acima com as informações do polo especifico.

#### POST
Deve Receber um objeto json no formato seguinte:

```json
{
    "data": {
        "add_estoque": 121
    }
}
```

A api busca na base dados o registro do polo baseado no nome da url, e soma o valor da chave "add_estoque" no campo
"estoque" do resgistro e Retorna o objeto JSON Único referente ao polo já atualizado. 
