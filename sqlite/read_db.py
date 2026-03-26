import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

# seleciona todos os dados da tabela estudantes
# * significa todos os campos
cursor.execute(
  """
    SELECT * FROM estudantes
  """
)

# seleciona todos os dados da tabela disciplinas
cursor.execute(
  """
    SELECT * FROM disciplinas
  """
)

conn.commit()

# armazena todos os dados da tabela estudantes na variável estudantes
estudantes = cursor.fetchall()

# armazena todos os dados da tabela disciplinas na variável disciplinas
disciplinas = cursor.fetchall()

# percorre a variável e imprime cada dado
for estudante in estudantes:
    print(estudante)

for disciplina in disciplinas:
    print(disciplina)

conn.close()