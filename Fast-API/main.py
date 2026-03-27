# Define as rotas e endpoints da aplicação

# Importa as bibliotecas necessárias
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import SessionLocal, engine

# Cria as tabelas no PostgreSQL (caso não existam)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Função para obter a sessão do banco de dados
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

# Cria uma rota com método POST para criar um estudante
# Função que recebe os dados do estudante e cria no banco de dados e é validado pelo schema.create
@app.post('/estudantes', response_model=schemas.EstudanteResponse)
def criar_estudante(estudante: schemas.EstudanteCreate, db: Session = Depends(get_db)):
  db_estudante = models.Estudante(**estudante.model_dump()) # Cria o objeto estudante
  db.add(db_estudante) # Adiciona o objeto estudante ao banco de dados
  db.commit() # Confirma a transação
  db.refresh(db_estudante) # Atualiza o objeto estudante com os dados do banco de dados
  return db_estudante # Retorna o objeto estudante