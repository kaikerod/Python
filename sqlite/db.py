import sqlite3

def conectar_db():
  conn = sqlite3.connect("escola.db")
  return conn

def criar_tabela_estudantes():
  conn = conectar_db()
  cursor = conn.cursor()
  cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS estudantes (
      id INTEGER PRIMARY KEY,
      nome TEXT,
      idade INTEGER
    )
    """)
  conn.commit()
  conn.close()

def criar_tabela_matriculas():
  conn = conectar_db()
  cursor = conn.cursor()
  cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS matriculas (
      id INTEGER PRIMARY KEY,
      nome_disciplina TEXT,
      estudante_id INTEGER,
      FOREIGN KEY (estudante_id) REFERENCES estudantes(id)
    )
    """)
  conn.commit()
  conn.close()

def inserir_estudante(nome, idade):
  conn = conectar_db()
  cursor = conn.cursor()
  cursor.execute(
    """
    INSERT INTO estudantes (nome, idade) 
    VALUES (?, ?)
    """, 
    (nome, idade)
  )
  conn.commit()
  conn.close()

def listar_estudantes():
  conn = conectar_db()
  cursor = conn.cursor()
  cursor.execute(
    """
    SELECT * FROM estudantes
    """
  )
  estudantes = cursor.fetchall()
  conn.close()
  return estudantes

def criar_matricula(nome_disciplina, estudante_id):
  conn = conectar_db()
  cursor = conn.cursor()
  cursor.execute(
    """
    INSERT INTO matriculas (nome_disciplina, estudante_id) 
    VALUES (?, ?)
    """, 
    (nome_disciplina, estudante_id)
  )
  conn.commit()
  conn.close()

def listar_matriculas():
  conn = conectar_db()
  cursor = conn.cursor()
  cursor.execute(
    """
      SELECT * FROM matriculas
    """
  )
  matriculas = cursor.fetchall()
  conn.close()
  return matriculas