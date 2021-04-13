# Sobre o desenvolvimento do Frontend

Foi utilizado o Framework [ReactJS](https://pt-br.reactjs.org/) juntamente com o [Bootstrap4](https://getbootstrap.com/)
para um template elegante e responsivo. Todos os cards gerados são baseados na resposta da API desenvolvida juntamente
com esta aplicação. A aplicação possui apenas um template sendo exibido, pois todas  as funcionalidades requisitadas
podem simplesmente ser exibidas numa única pagina. uma requisição na raiz da URL  redireciona para o /polos.



# Sobre o funcionamento da aplicação


## Legendas

#### COBERTURA IDEAL
A legenda "VERDE" indica que o estoque atual do polo irá durar entre 14 e 18 dias, baseado no
consumo médio diário informado pela API.

#### ATENÇÃO
A legenda "AMARELA" indica que o estoque atual do polo irá durar entre 10 e 13 dias ou 19 e 23 dias, baseado no
consumo médio diário informado pela API.

#### PERIGO
A legenda "VERMELHO" indica que o estoque atual do polo irá durar menos de 10 dias ou mais de 23 dias, baseado no
consumo médio diário informado pela API.


## Cards

Cada Card representa um polo, sendo exibido explicitamente seu estoque atual e seu consumo médio diário.
Ainda no card é exibido a opção de ordem de expedição, que exibe quantos terminais precisam ser enviados para que
o polo Receba legenda "VERDE" de cobertura ideal.

A aplicação não o obriga a enviar aquele mesmo número de termianis, ele apenas sugere. Caso confirme
o envio de um número qualquer de terminais uma requisição POST é enviada a api, o dialogo se fecha e fica em aguardo a
reposta da api, e baseado nesta resposta a aplicação atualiza o card.
