import falcon

from auxiliarLogistica.api.base import BaseResource
from auxiliarLogistica.api.util import load_bases, load_bases_json,\
    update_base


# / retorna uma mensagem amigavel de boas vindas à api :)
class IndexResource(BaseResource):
    def on_get(self, req, resp):
        if req.path == "/":
            resp.status = falcon.HTTP_200
            resp.body = self.to_json(self.HELLO)


# /polos (retorna uma lista com todos os polos)
class PolosResource(BaseResource):
    polos = load_bases()

    def on_get(self, req, resp):
        resp.body = self.to_json(self.polos)
        resp.status = falcon.HTTP_200

    # recebe um dict com a base atualizada
    # busca na lista e atualiza a mesma
    def update_base(self, up_base):
        index = 0
        for polo in self.polos:
            if polo['id'] == up_base['id']:
                self.polos[index] = up_base
                break
            index += 1


# /polos/{polo} (retorna o estoque deste polo + nome + media-de-consumo-diaria)
class PoloEstoqueResource(BaseResource):
    polos_json = load_bases_json()
    polos_instance = None

    def on_get(self, req, resp, polo):
        if polo in self.polos_json:
            resp.body = self.to_json(self.polos_json[polo])
            resp.status = falcon.HTTP_200
        else:
            message = "sorry, didn't find this :("
            resp = self.on_not_found(resp, message)

    # deve receber um json {'add_estoque': n_terminals}
    # a aplicação react informa o numero mais apropriado
    def on_post(self, req, resp, polo):
        if polo in self.polos_json:
            try:
                context = self.from_json(req.stream.read())['data']
                add_estoque = context['add_estoque']

                self.update_base_estoque(polo, add_estoque)

                resp.body = self.to_json(self.polos_json[polo])
                resp.status = falcon.HTTP_200
            except KeyError:
                resp.body = self.to_json({
                    "msg": "json format invalid",
                    "error": "KeyError"
                })
                resp.status = falcon.HTTP_400
            except ValueError:
                resp.body = self.to_json({
                    "msg": "only integers in 'add_estoque' are processed",
                    "error": "TypeError"
                })
                resp.status = falcon.HTTP_400

        else:
            message = "sorry, didn't find this :("
            resp = self.on_not_found(resp, message)

    # atualiza a base de dados de acordo com a solicitação
    def update_base_estoque(self, base, add_estoque):
        self.polos_json[base]['estoque'] += int(add_estoque)
        update_base(self.polos_json[base])

        self.update_polos_instance(self.polos_json[base])

    # atualiza a base na instancia da classe PolosResource
    def update_polos_instance(self, base):
        self.polos_instance.update_base(base)
