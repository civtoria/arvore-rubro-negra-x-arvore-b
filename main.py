import random
from db_utils import criar_conexao, ler_dados_db
from arvores_utils import popular_estrutura, buscar_chaves
from timer_utils import medir_tempo
from sortedcontainers import SortedDict  # Red-Black Tree (aproximada)
from bintrees import FastRBTree  # B-Tree

# Configuração da conexão com o banco de dados
usuario = 'root'
senha = '190827'
host = 'localhost'
porta = '3306'  # Porta padrão para MySQL
banco_de_dados = 'employees'

# Criação da conexão
conexao = criar_conexao(usuario, senha, host, porta, banco_de_dados)

# Consulta SQL para obter os dados
consulta_sql = 'SELECT emp_no, dept_no FROM dept_emp'

# Ler dados do banco de dados
dados = ler_dados_db(conexao, consulta_sql)

# Gerar chaves de busca aleatórias
tamanho_dados = len(dados)
chaves_busca = [random.randint(0, tamanho_dados * 10) for _ in range(1000)]

# Comparando inserção e busca na Red-Black Tree (SortedDict)
rbt_estrutura = SortedDict()
_, tempo_insercao_rbt = medir_tempo(popular_estrutura, rbt_estrutura, dados)
_, tempo_busca_rbt = medir_tempo(buscar_chaves, rbt_estrutura, chaves_busca)

# Comparando inserção e busca na B-Tree (FastRBTree)
btree_estrutura = FastRBTree()
_, tempo_insercao_btree = medir_tempo(popular_estrutura, btree_estrutura, dados)
_, tempo_busca_btree = medir_tempo(buscar_chaves, btree_estrutura, chaves_busca)

# Exibindo os resultados
print(f"Tempo de insercao na Arvore Rubro-Negra: {tempo_insercao_rbt:.4f} segundos")
print(f"Tempo de busca na Arvore Rubro-Negra: {tempo_busca_rbt:.4f} segundos")
print(f"Tempo de insercao na Arvore B: {tempo_insercao_btree:.4f} segundos")
print(f"Tempo de busca na Arvore B: {tempo_busca_btree:.4f} segundos")