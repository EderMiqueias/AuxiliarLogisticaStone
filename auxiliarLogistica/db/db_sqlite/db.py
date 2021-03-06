from .util import db_exist_data, insert_data_atendimentos,\
    insert_data_bases, create_tables, insert_from_csv,\
    get_atendimentos, get_bases, update_base


# retorna uma lista de dicts
def get(table) -> list:
    if table == "atendimentos":
        data = get_atendimentos()
    else:
        data = get_bases()
    return data


# recebe uma lista de dicts e a tabela de inserção
# insere na tabela informada
def insert(data, table) -> None:
    if table == "bases":
        insert_data_bases(data)
    elif table == "atendimentos":
        insert_data_atendimentos(data)


# Recebe um objeto dict atualizado
def update(data) -> None:
    update_base(data)
    return


# responsavel por, caso haja um db e possua dados nele:
# - solicitar a criação das tabelas
# - solicitar a inserção dos dados nelas, a partir do csv
def migrate() -> None:
    if db_exist_data():
        return
    create_tables()
    insert_from_csv("atendimentos_desafio_stone.csv", "atendimentos")
    insert_from_csv("estoque_bases_desafio_stone.csv", "bases")
