import sqlite3

def conectar_db():
  conn = sqlite3.connect("loja.db")
  return conn

def criar_tabela_produtos():
  conn = conectar_db()
  cursor = conn.cursor()
  cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS tabela_produtos (
      id INTEGER PRIMARY KEY,
      nome TEXT,
      preco REAL
    )
    """
  )
  conn.commit()
  conn.close()

def inserir_produto():
  conn = conectar_db()
  cursor = conn.cursor()
  cursor.execute(
    """
    INSERT INTO tabela_produtos (nome, preco) 
    VALUES (?, ?)
    """
  )
  conn.commit()
  conn.close()

def listar_produtos_cadastrados():
  conn = conectar_db()
  cursor = conn.cursor()
  cursor.execute(
    """
    SELECT * FROM tabela_produtos
    """
  )
  produtos = cursor.fetchall()
  conn.close()
  return produtos