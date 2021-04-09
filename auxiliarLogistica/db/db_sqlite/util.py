import sqlite3
import auxiliarLogistica.db.db_csv as db_csv

DB_NAME = "db.sqlite3"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


# retorna True se houver tabelas no db
def db_exist_data() -> bool:
    return _db_exist_data()


# Retorna uma lista de objetos dict
def get_bases() -> list:
    cursor.execute("""
    SELECT base, estoque FROM bases;
    """)

    indexes = ['base', 'estoque']
    bases = db_csv.to_json_list(indexes, cursor.fetchall())

    return bases


# Retorna uma lista de objetos dict
def get_atendimentos() -> list:
    cursor.execute("""
        SELECT date, base, country_state, consumption FROM atendimentos;
        """)

    indexes = ['date', 'base', 'country_state', 'consumption']
    atends = db_csv.to_json_list(indexes, cursor.fetchall())

    return atends


# recebe uma lista de dicts e a tabela de inserção
# insere na tabela informada
def insert_data(data, table) -> None:
    if table == "bases":
        insert_data_bases(data)
    elif table == "atendimentos":
        insert_data_atendimentos(data)

    _commit()


# recebe uma str com o endereço do arquivo csv
# responsavel pela migração de dados do arquivo csv para o db
# caso o db esteja vazio
def insert_from_csv(file_url, table) -> None:
    data = db_csv.get_from_csv(file_url)
    insert_data(data, table)
    return


# recebe uma lista de dicts
def insert_data_atendimentos(data) -> None:
    for atend in data:
        cursor.execute(
            "INSERT INTO atendimentos (date, base, country_state, consumption)"
            + "VALUES (?, ?, ?, ?);",
            (atend['date'], atend['base'], atend['country_state'], atend['consumption'])
        )
    return


# recebe uma lista de dicts
def insert_data_bases(data) -> None:
    for base in data:
        cursor.execute(
            "INSERT INTO bases (base, estoque)"
            + "VALUES (?, ?);",
            (base['base'], base['estoque'])
        )
    return


# !usar o id no where seria aforma correta, porém, como não há
# polos iguais optei por usar o nome do polo como identificador!
# Recebe um objeto dict atualizado
def update_base(data) -> None:
    cursor.execute(
        "UPDATE bases SET estoque = ? WHERE base = ?",
        (data['estoque'], data['base'])
    )

    _commit()


# responsavel por criar as tabelas necessarias
def create_tables() -> None:
    _create_table_bases()
    _create_table_atendimentos()

    _commit()


# responsavel por criar a tabela bases
def _create_table_bases() -> None:
    cursor.execute(
        "CREATE TABLE bases ("
        + "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
        + "base TEXT NOT NULL,"
        + "estoque INTEGER NOT NULL"
        + ");"
    )


# responsavel por criar a tabela atendimentos
def _create_table_atendimentos() -> None:
    cursor.execute(
        "CREATE TABLE atendimentos ("
        + "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
        + "date TEXT NOT NULL,"
        + "base TEXT NOT NULL,"
        + "country_state TEXT NOT NULL,"
        + "consumption TEXT NOT NULL);"
    )


# retorna True se houver dados regiistrados no db
def _db_exist_data() -> bool:
    try:
        cursor.execute("SELECT base FROM bases")
        return True
    except sqlite3.OperationalError:
        return False


def _commit() -> None:
    conn.commit()
    return
