import falcon

from auxiliarLogistica.api.base import BaseResource
from auxiliarLogistica.api.util import load_bases, load_bases_json,\
    load_atendimentos_json


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


# /polos/{polo} (retorna o estoque deste polo + nome)
class PoloEstoqueResource(BaseResource):
    polos_json = load_bases_json()
    atendimentos_json = load_atendimentos_json()

    def on_get(self, req, resp, polo):
        if polo in self.polos_json:
            resp.body = self.to_json(
                self._insert_average(self.polos_json[polo])
            )
            resp.status = falcon.HTTP_200
        else:
            message = "sorry, didn't find this :("
            resp = self.on_not_found(resp, message)

    # insere a chave 'average' no dict com a media de consumo diario
    def _insert_average(self, obj) -> dict:
        b = self.atendimentos_json[obj["base"]]
        average = b['terminals'] / len(b["days"])
        obj["average"] = average
        return obj

