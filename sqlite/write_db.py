import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

# Inserindo dados na tabela estudantes
cursor.execute(
  """
    INSERT INTO estudantes (nome, idade) 
    VALUES (?, ?)
  """, 
  ("Kaike", 20)
)

cursor.execute(
  """
    INSERT INTO disciplinas (estudante_id, nome_disciplina) 
    VALUES (?, ?)
  """, 
  (1, "Matemática")
)

conn.commit()
conn.close()