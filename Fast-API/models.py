# Define as entidades da aplicação, ex: produtos, clientes, etc.

from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Estudante(Base):
  __tablename__ = "estudantes"
  id = Column(Integer, primary_key=True, index=True) # index=True cria um índice que automaticamente incrementa o valor
  nome = Column(String(100), nullable=False) # nullable=False significa que o campo não pode ser nulo e String(100) define o tamanho máximo do campo
  idade = Column(Integer, nullable=False)

class Matricula(Base):
  __tablename__ = "matriculas"
  id = Column(Integer, primary_key=True, index=True)
  estudante_id = Column(Integer, ForeignKey("estudantes.id"))
  nome_disciplina = Column(String(100), nullable=False)