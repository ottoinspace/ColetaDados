import pymysql
import pandas as pd
from sqlalchemy import create_engine


def conexao_mysql(host, user, password, db, table):
    # Criar conexao
    conn = pymysql.connect(host=host, user=user, password=password, db=db)

    cursor = conn.cursor()

    # Executar consulta
    query = 'SELECT * FROM' + table + ' limit 10'
    cursor.execute(query)

    # Buscar resultados
    resultados = cursor.fetchall()

    # Exebir resultados
    print('Tabela MySQL:')
    for linha in resultados:
        print(linha)

    # Fechar a conexao
    cursor.close()
    conn.close()


def df_conexao_mysql(host, user, password, db, table):
    # Criar Conexao
    conn = create_engine('mysql+pymysql://' + user + ':' + password + '@' + host + '/' + db)
    # conn = pymysql.connect(host=host, user=user, password=password, db=db)

    # Executar consulta e salvar em um dataframe
    query = 'SELECT * FROM' + table
    df = pd.read_sql(query, conn)

    # Exibir os resultados
    print('Table MYSQL com DataFrame: \n', df.head())

    # Fechar conexao
    conn.dispose()
    # conn.close()
    return df


def conexao_excel(path):
    # Ler arquivo Excel
    df = pd.read_excel(path)
    print('Dados Excel: \n', df.head())

    # Escrever arquivo CSV
    df.to_csv('dados.csv', index=False)


def conexao_csv(path):
    # Ler arquivo CSV
    df = pd.read_csv(path)
    print('Dados CSV: \n', df.head())

    # Escrever arquivo JSON
    df.to_json('dados.json', orient='records', index=False)
