import falcon
from falcon_cors import CORS

from auxiliarLogistica.api.resources import IndexResource,\
    PolosResource, PoloEstoqueResource

cors = CORS(allow_all_origins=True)

application = falcon.API(middleware=[cors.middleware])
polos = PolosResource()
estoque = PoloEstoqueResource()
index = IndexResource()


application.add_route('/', index)
application.add_route('/polos', polos)
application.add_route('/polos/{polo}', estoque)
