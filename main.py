from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Identifier
from schemas import IdentifierCreate, IdentifierResponse, IdentifierUpdate

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API works"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/identifiers/", response_model=IdentifierResponse)
def create_identifier(identifier: IdentifierCreate, db: Session = Depends(get_db)):
    db_identifier = Identifier(**identifier.model_dump())
    db.add(db_identifier)
    db.commit()
    db.refresh(db_identifier)
    return db_identifier


@app.get("/identifiers/", response_model=list[IdentifierResponse])
def get_identifiers(db: Session = Depends(get_db)):
    return db.query(Identifier).all()


@app.get("/identifiers/{identifier_name}", response_model=IdentifierResponse)
def get_identifier(identifier_name: str, db: Session = Depends(get_db)):
    identifier = db.query(Identifier).filter(Identifier.identifier_name == identifier_name).first()
    if not identifier:
        raise HTTPException(status_code=404, detail="Identifier not found")
    return identifier


@app.put("/identifiers/{identifier_name}", response_model=IdentifierResponse)
def update_identifier(identifier_name: str, identifier_data: IdentifierUpdate, db: Session = Depends(get_db)):
    identifier = db.query(Identifier).filter(Identifier.identifier_name == identifier_name).first()
    if not identifier:
        raise HTTPException(status_code=404, detail="Identifier not found")

    update_data = identifier_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(identifier, key, value)

    db.commit()
    db.refresh(identifier)
    return identifier


@app.delete("/identifiers/{identifier_name}")
def delete_identifier(identifier_name: str, db: Session = Depends(get_db)):
    identifier = db.query(Identifier).filter(Identifier.identifier_name == identifier_name).first()
    if not identifier:
        raise HTTPException(status_code=404, detail="Identifier not found")

    db.delete(identifier)
    db.commit()
    return {"message": "Identifier deleted successfully"}