import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

# Inserindo dados na tabela estudantes
cursor.execute("""
    INSERT INTO estudantes (nome, idade) 
    VALUES (?, ?)
""", ("Kaike", 20))

conn.commit()
conn.close()