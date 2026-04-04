from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from database import Base

class Livro(Base):
    __tablename__ = "livros"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    autor = Column(String)
    ano = Column(Integer)
    genero = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean, default=True)