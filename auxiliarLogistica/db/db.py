from .db_sqlite import get, migrate, update


# Retorna uma lista de objetos dict
# a migração só ocorre caso o db esteja vazio
def get_atendimentos() -> list:
    migrate()
    return get("atendimentos")


# Retorna uma lista de objetos dict
# a migração só ocorre caso o db esteja vazio
def get_estoque_bases() -> list:
    migrate()
    return get("bases")


# Recebe um objeto dict atualizado
def update_estoque_base(updated_base) -> None:
    update(updated_base)
    return
