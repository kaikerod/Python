from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal
from typing import List
from sqlalchemy.orm import joinedload

app = FastAPI() 

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/estudantes", response_model=schemas.Estudante)
def criar_estudante(estudante: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    db_estudante = models.Estudante(nome=estudante.nome, perfil=models.Perfil(**estudante.perfil.dict()))
    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)
    return db_estudante

@app.get("/estudantes", response_model=List[schemas.Estudante])
def listar_estudantes(db: Session = Depends(get_db)):
    estudantes = db.query(models.Estudante).options(joinedload(models.Estudante.perfil)).all()
    return estudantes

@app.delete("/estudantes/{id}", response_model=schemas.Estudante)
def deletar_estudante(id: int, db: Session = Depends(get_db)):
    estudante = db.query(models.Estudante).filter(models.Estudante.id == id).first()
    if not estudante:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    db.delete(estudante)
    db.commit()
    return estudante

@app.post("/professores", response_model=schemas.Professor)
def criar_professor(professor: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    db_professor = models.Professor(nome=professor.nome, especialidade=professor.especialidade)
    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
    return db_professor

@app.get("/professores", response_model=List[schemas.Professor])
def listar_professores(db: Session = Depends(get_db)):
    professores = db.query(models.Professor).all()
    return professores

@app.delete("/professores/{id}", response_model=schemas.Professor)
def deletar_professor(id: int, db: Session = Depends(get_db)):
    professor = db.query(models.Professor).filter(models.Professor.id == id).first()
    if not professor:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    db.delete(professor)
    db.commit()
    return professor