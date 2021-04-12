import falcon
from falcon_cors import CORS

from auxiliarLogistica.api.resources import IndexResource,\
    PolosResource, PoloEstoqueResource

cors = CORS(allow_all_origins=True, allow_all_methods=True, allow_all_headers=True)

application = falcon.API(middleware=[cors.middleware])

index = IndexResource()
polos = PolosResource()

estoque = PoloEstoqueResource()
estoque.polos_instance = polos

application.add_route('/', index)
application.add_route('/polos', polos)
application.add_route('/polos/{polo}', estoque)
