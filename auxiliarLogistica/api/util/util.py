from auxiliarLogistica.db import get_estoque_bases


# Retorna uma lista com os dicts de cada polo
# adiciona aos dicts um novo campo url
def load_bases() -> list:
    return list(map(lambda d: _add_url(d), get_estoque_bases()))


# Retorna um dict tendo o nome dos polos como chave e um dict como valor
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
