import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

# atualiza os dados da tabela estudantes
# SET nome = ?, idade = ? -> define os novos valores para os campos nome e idade
# WHERE id = ? -> define a condição para a atualização e o id que será atualizado
cursor.execute(
  """
    UPDATE estudantes SET nome = ?, idade = ?
    WHERE id = ?
  """, 
  ("Leandro", 16, 2)
)

conn.commit()
conn.close()