from typing import Optional
from pydantic import BaseModel


class Perfil(BaseModel):
    id: int
    idade: int
    endereco: str

    class Config:
        from_attributes = True

class PerfilCreate(BaseModel):
    idade: int
    endereco: str

class Estudante(BaseModel):
    id: int
    nome: str
    perfil: Optional[Perfil] = None

    class Config:
        from_attributes = True

class EstudanteCreate(BaseModel):
    id: int
    nome: str
    perfil: PerfilCreate

class Professor(BaseModel):
    id: int
    nome: str
    especialidade: str

    class Config:
        from_attributes = True

class ProfessorCreate(BaseModel):
    nome: str
    especialidade: str