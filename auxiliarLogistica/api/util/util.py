from auxiliarLogistica.db import get_estoque_bases, get_atendimentos


# retorna uma lista com os dicts de cada polo
# adiciona aos dicts um novo campo url
def load_bases() -> list:
    return list(map(lambda d: _add_url(d), get_estoque_bases()))


# retorna um dict tendo os polos como chave e seus respectivos
# dias de ordem de serviço e terminais entregues
def load_atendimentos_json() -> dict:
    atends_json = _get_atendimentos_json()
    return atends_json


# retorna um dict tendo o nome dos polos como chave e um dict como valor
def load_bases_json() -> dict:
    bases_json = dict()
    for b_json in get_estoque_bases():
        b_json = _add_url(b_json)
        bases_json[b_json['url']] = b_json
    return bases_json


# adiciona a chave url com o valor da base em lower case e sem espaços
def _add_url(obj) -> dict:
    obj['url'] = obj['base'].replace(" ", "").lower()
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
