# Recebe uma lista com o nome dos indexes e um objeto iteravel composto
# por varias listas, cujas devem ter o mesmo coprimento da primeira
# isso é necessário para a transposição
# Retorna umma lista de objetos dict
def to_json_list(indexes, data) -> list:
    json_list = list()
    indexes = list(map(lambda x: x.lower(), indexes))
    for item in data:
        json_list.append(dict(zip(indexes, item)))
    return json_list


# aplicavel ao dataset retornado do get_from_csv
def _str_to_int(obj, keys) -> dict:
    for key in keys:
        obj[key] = int(obj[key])
    return obj
