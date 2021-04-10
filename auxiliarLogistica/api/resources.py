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


# /polos/{polo} (retorna o estoque deste polo + nome + media-de-consumo-diaria)
class PoloEstoqueResource(BaseResource):
    polos_json = load_bases_json()

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
            context = self.from_json(req.stream.read())['data']
            add_estoque = context['add_estoque']
            self.polos_json[polo]['estoque'] += add_estoque

            update_base(self.polos_json[polo])

            resp.body = self.to_json(self.polos_json[polo])
            resp.status = falcon.HTTP_200
        else:
            message = "sorry, didn't find this :("
            resp = self.on_not_found(resp, message)
