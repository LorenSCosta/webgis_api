# app/property/property_controller.property
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from typing import List
from database import SessionLocal
from . import property_service, property_model

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/property", tags=["Property"])

@router.post("/save", response_model=property_model.PropertyPublic, status_code=status.HTTP_201_CREATED)
def create_property(property: property_model.PropertyCreate, db: Session = Depends(get_db)):
    """Endpoint para criar uma nova propriedade. Recebe os dados validados (property)
    e a sessão do banco (db) através da injeção de dependência."""
    return property_service.create_new_property(db=db, property=property)



@router.get("/", response_model=List[property_model.PropertyPublic])
def read_property(db: Session = Depends(get_db)):
    
    return property_service.get_all_property(db)

@router.get("/{property_id}", response_model=property_model.PropertyPublic)
def read_property(property_id: int, db: Session = Depends(get_db)):
   
    return property_service.get_property_by_id(db, property_id=property_id)

@router.put("/{property_id}", response_model=property_model.PropertyPublic)
def update_property(property_id: int, property: property_model.PropertyUpdate, db: Session = Depends(get_db)):
    
    return property_service.update_existing_property(db=db, property_id=property_id, property_in=property)

@router.delete("/{property_id}", response_model=property_model.PropertyPublic)
def delete_property(property_id: int, db: Session = Depends(get_db)):
   
    return property_service.delete_property_by_id(db=db, property_id=property_id)

