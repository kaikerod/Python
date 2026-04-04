from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal
from typing import List
from sqlalchemy.orm import joinedload

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/livros", response_model=schemas.Livro)
def create_livro(livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    db_livro = models.Livro(**livro.dict())
    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro

@app.get("/livros", response_model=List[schemas.Livro])
def read_livros(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    livros = db.query(models.Livro).offset(skip).limit(limit).all()
    return livros

@app.get("/livros/{livro_id}", response_model=schemas.Livro)
def read_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()
    if livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro

@app.put("/livros/{livro_id}", response_model=schemas.Livro)
def update_livro(livro_id: int, livro: schemas.LivroUpdate, db: Session = Depends(get_db)):
    db_livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()
    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    for field, value in livro.dict().items():
        setattr(db_livro, field, value)
    db.commit()
    db.refresh(db_livro)
    return db_livro

@app.delete("/livros/{livro_id}", response_model=schemas.Livro)
def delete_livro(livro_id: int, db: Session = Depends(get_db)):
    db_livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()
    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    db.delete(db_livro)
    db.commit()
    return db_livro