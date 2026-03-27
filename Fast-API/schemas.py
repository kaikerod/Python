# Valida os dados que chegam na API

from pydantic import BaseModel

# Garante que os dados que chegam na API estão corretos, ex: nome é string e idade é int
class EstudanteBase(BaseModel):
  nome: str
  idade: int

class EstudanteCreate(EstudanteBase):
  pass

# Herda de EstudanteBase e adiciona o campo id
class EstudanteResponse(EstudanteBase):
  id: int

  class Config:
    from_attributes = True # Informa para o Pydantic que ele deve ler os atributos do modelo SQLAlchemy

class MatriculaBase(BaseModel):
  estudante_id: int
  nome_disciplina: str

class MatriculaCreate(MatriculaBase):
  pass

class MatriculaResponse(MatriculaBase):
  id: int

  class Config:
    from_attributes = True
