import falcon

from auxiliarLogistica.api.base import BaseResource
from auxiliarLogistica.api.util import load_bases, load_bases_json


# / (retorna uma mensagem amigavel de boas vindas a api :))
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


# /polos/{polo} (retorna o estoque deste polo + nome)
class PoloEstoqueResource(BaseResource):
    polos_json = load_bases_json()

    def on_get(self, req, resp, polo):
        if polo in self.polos_json:
            resp.body = self.to_json(self.polos_json[polo])
            resp.status = falcon.HTTP_200
        else:
            message = "sorry, didn't find this :("
            resp = self.on_not_found(resp, message)


# /polos/{polo} (retorna todos os atendimentos deste polo)
