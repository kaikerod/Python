import sqlite3

conn = sqlite3.connect("hotel_plus.db")
cursor = conn.cursor()

cursor.execute(
  """
    CREATE TABLE IF NOT EXISTS usuarios (
      id INTEGER PRIMARY KEY,
      nome TEXT,
      email TEXT
    )
  """
)

cursor.execute(
  """
    INSERT INTO usuarios (nome, email) 
    VALUES (?, ?)
  """, 
  ("Kaike", "[EMAIL_ADDRESS]")
)

cursor.execute(
  """
    INSERT INTO usuarios (nome, email) 
    VALUES (?, ?)
  """, 
  ("Ana", "[EMAIL_ADDRESS]")
)

cursor.execute(
  """
    SELECT * FROM usuarios
  """
)

usuarios = cursor.fetchall()

for usuario in usuarios:
  print(usuario)

conn.commit()
conn.close()