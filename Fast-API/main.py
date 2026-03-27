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

# Cria uma rota com método GET para buscar estudantes
# Retorna uma lista de estudantes
@app.get('/estudantes', response_model=List[schemas.EstudanteResponse])
def ler_estudantes(db: Session = Depends(get_db)): # Retorna uma sessão do banco de dados
  estudantes = db.query(models.Estudante).all() # Busca todos os estudantes
  return estudantes # Retorna todos os estudantes

@app.post('/matriculas', response_model=schemas.MatriculaResponse)
def criar_matricula(matricula: schemas.MatriculaCreate, db: Session = Depends(get_db)):
  db_matricula = models.Matricula(**matricula.model_dump())
  db.add(db_matricula)
  db.commit()
  db.refresh(db_matricula)
  return db_matricula

@app.get('/matriculas', response_model=List[schemas.MatriculaResponse])
def ler_matriculas(db: Session = Depends(get_db)):
  matriculas = db.query(models.Matricula).all()
  return matriculas

@app.delete('/estudantes/{estudante_id}') # Deleta um estudante pelo id
def deletar_estudante(estudante_id: int, db: Session = Depends(get_db)): # Recebe o id do estudante e uma sessão do banco de dados
  db_estudante = db.query(models.Estudante).filter(models.Estudante.id == estudante_id).first() # Busca o estudante pelo id
  if not db_estudante: # Se o estudante não for encontrado
    raise HTTPException(status_code=404, detail="Estudante não encontrado") # Retorna um erro 404
  db.delete(db_estudante) # Deleta o estudante
  db.commit() # Confirma a transação
  return {"message": "Estudante deletado com sucesso"}

@app.delete('/matriculas/{matricula_id}') # Deleta uma matrícula pelo id
def deletar_matricula(matricula_id: int, db: Session = Depends(get_db)): # Recebe o id da matrícula e uma sessão do banco de dados
  db_matricula = db.query(models.Matricula).filter(models.Matricula.id == matricula_id).first() # Busca a matrícula pelo id
  if not db_matricula: # Se a matrícula não for encontrada
    raise HTTPException(status_code=404, detail="Matrícula não encontrada") # Retorna um erro 404
  db.delete(db_matricula) # Deleta a matrícula
  db.commit() # Confirma a transação
  return {"message": "Matrícula deletada com sucesso"}

@app.get('/estudantes/{estudante_id}', response_model=schemas.EstudanteResponse)
def ler_estudante(estudante_id: int, db: Session = Depends(get_db)):
  estudante = db.query(models.Estudante).filter(models.Estudante.id == estudante_id).first()
  if not estudante:
    raise HTTPException(status_code=404, detail="Estudante não encontrado")
  return estudante
