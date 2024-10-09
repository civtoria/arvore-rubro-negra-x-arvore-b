import pandas as pd
from sqlalchemy import create_engine

def criar_conexao(usuario, senha, host, porta, banco_de_dados):
    conexao_str = f'mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco_de_dados}'
    return create_engine(conexao_str)

def ler_dados_db(conexao, consulta):
    df = pd.read_sql(consulta, conexao)
    return list(df.itertuples(index=False, name=None))