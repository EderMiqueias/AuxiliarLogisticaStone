from auxiliarLogistica.db import get_estoque_bases,\
    get_atendimentos, update_estoque_base


# retorna uma lista com os dicts de cada polo
# adiciona aos dicts um novo campo url
def load_bases() -> list:
    atendimentos = load_atendimentos_json()
    return list(map(
        lambda d: _insert_url_average(d, atendimentos),
        get_estoque_bases()
    ))


# retorna um dict tendo os polos como chave e seus respectivos
# dias de ordem de serviço e terminais entregues
def load_atendimentos_json() -> dict:
    atends_json = _get_atendimentos_json()
    return atends_json


# retorna um dict tendo o nome dos polos como chave e um dict como valor
def load_bases_json() -> dict:
    bases_json = dict()
    atendimentos = load_atendimentos_json()

    for b_json in get_estoque_bases():
        b_json = _insert_url_average(b_json, atendimentos)
        bases_json[b_json['url']] = b_json
    return bases_json


# recebe um dict com a base atualizada
def update_base(base) -> None:
    update_estoque_base(base)
    return


# adiciona a chave url com o valor da base em lower case e sem espaços
# insere a chave 'average' no dict com a media de consumo diario
def _insert_url_average(obj, atendimentos) -> dict:
    b = atendimentos[obj["base"]]
    average = b['terminals'] / len(b["days"])

    obj['url'] = obj['base'].replace(" ", "").lower()
    obj["average"] = average

    return obj


# retorna um dict na seguinte estrutura
# {
#     "base_name": {
#         "days": "dias com ordem de serviço",
#         "terminals": "total de terminais entregues pelo polo"
#     }...
# }
def _get_atendimentos_json() -> dict:
    atends_json = dict()
    for base in get_estoque_bases():
        atends_json[base["base"]] = {
            "days": set(),
            "terminals": 0,
        }

    for a_json in get_atendimentos():
        atends_json[a_json['base']]["days"].add(a_json['date'])
        atends_json[a_json['base']]["terminals"] += 1
    return atends_json
