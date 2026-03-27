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