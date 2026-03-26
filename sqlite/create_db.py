import sqlite3

# cria conexão com o banco de dados/cria o arquivo escola.db se não existir
conn = sqlite3.connect("escola_1.db")

# cria cursor para executar comandos sql
cursor = conn.cursor()

# cria tabela alunos
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER
)
""")

# cria tabela disciplinas
# FOREIGN KEY (estudante_id) REFERENCES estudantes(id) -> cria relação entre as tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS disciplinas (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    estudante_id INTEGER,
    FOREIGN KEY (estudante_id) REFERENCES estudantes(id)
)
""")

#confirma as alterações
conn.commit()
#fecha a conexão
conn.close()