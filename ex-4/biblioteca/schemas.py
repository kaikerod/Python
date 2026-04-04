from typing import Optional
from pydantic import BaseModel

class LivroBase(BaseModel):
    titulo: str
    autor: str
    ano: int
    genero: str
    preco: float
    disponivel: bool = True

class LivroCreate(LivroBase):
    pass

class LivroUpdate(LivroBase):
    pass

class Livro(LivroBase):
    id: int

    class Config:
        from_attributes = True