from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Estudante(Base):
    __tablename__ = "estudantes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    perfil = relationship("Perfil", back_populates="estudante", uselist=False, cascade="all, delete-orphan") # Relacionamento entre estudante e perfil
# Uselist=False indica que o relacionamento é de um para um
# Back_populates indica que o relacionamento é bidirecional entre estudante e perfil
# Cascade="all, delete-orphan" indica que o relacionamento é de um para um, se o estudante for deletado, o perfil também será deletado

class Perfil(Base):
    __tablename__ = "perfis"
    id = Column(Integer, primary_key=True, index=True)
    idade = Column(Integer)
    endereco = Column(String)
    estudante_id = Column(Integer, ForeignKey("estudantes.id"), unique=True)
    estudante = relationship("Estudante", back_populates="perfil")
# Unique=True indica que o perfil só pode ter um estudante
# Back_populates indica que o relacionamento é bidirecional entre estudante e perfil

class Professor(Base):
    __tablename__ = "professores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    especialidade = Column(String)
    cursos = relationship("Curso", back_populates="professor", cascade="all, delete-orphan")
# Cascade="all, delete-orphan" indica que o relacionamento é de um para muitos, se o professor for deletado, os cursos também serão deletados