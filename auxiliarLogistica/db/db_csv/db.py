import csv
from .util import to_json_list


# Recebe o local de um arquivo csv que servirá como base de dados
# Retorna uma lista de objetos dict
def get_from_csv(file_url) -> list:
    with open(file_url, 'r', newline='') as f:
        data = csv.reader(f, delimiter=";")
        data = to_json_list(data.__next__(), data)

        f.close()
        return data
