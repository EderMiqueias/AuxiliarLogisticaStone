import csv


# Retorna uma lista de objetos dict
def get_atendimentos() -> list:
    return get_from_csv("atendimentos_desafio_stone.csv")


# Retorna uma lista de objetos dict
def get_estoque_bases() -> list:
    return get_from_csv("estoque_bases_desafio_stone.csv")


# Recebe o local de um arquivo csv que servirá coo base de dados
# Retorna uma lista de objetos dict
def get_from_csv(file_url) -> list:
    with open(file_url, 'r', newline='') as f:
        data = csv.reader(f, delimiter=";")
        data = _to_json_list(data.__next__(), data)

        f.close()
        return data


# Recebe uma lista com o nome dos indexes e um objeto iteravel composto
# por varias listas, cujas devem ter o mesmo coprimento da primeira
# isso é necessário para a transposição
# Retorna umma lista de objetos dict
def _to_json_list(indexes, data) -> list:
    json_list = list()
    indexes = list(map(lambda x: x.lower(), indexes))
    for item in data:
        json_list.append(dict(zip(indexes, item)))
    return json_list
