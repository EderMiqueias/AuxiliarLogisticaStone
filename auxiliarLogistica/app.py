import falcon

from auxiliarLogistica.api.resources import IndexResource,\
    PolosResource, PoloEstoqueResource


application = falcon.API()
polos = PolosResource()
estoque = PoloEstoqueResource()
index = IndexResource()


application.add_route('/', index)
application.add_route('/polos', polos)
application.add_route('/polos/{polo}', estoque)
