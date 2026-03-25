import sqlite3
import os

# Define o caminho para o banco de dados na mesma pasta do script
db_path = os.path.join(os.path.dirname(__file__), "escola.db")

# Conectando ao banco de dados
# Se o banco de dados não existir, ele será criado no caminho especificado
conn = sqlite3.connect(db_path)
# conn = sqlite3.connect("escola.db")

# Executa tarefas no banco de dados
cursor = conn.cursor()

# Criando a tabela alunos
cursor.execute("""
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER
)
""")

# Inserindo dados na tabela
cursor.execute("INSERT INTO alunos (nome, idade) VALUES (?, ?)", ("Joao", 20))

# Salvando as alterações
conn.commit()

# Buscando dados na tabela
cursor.execute("SELECT * FROM alunos")
print(cursor.fetchall())

# Fechando a conexão
conn.close()