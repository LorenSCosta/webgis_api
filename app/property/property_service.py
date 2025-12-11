from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.property import property_repository
from app.property.property_model import PropertyCreate, PropertyUpdate


def create_new_property(db: Session, property: PropertyCreate):
    # Aqui você pode adicionar validações de negócio (por exemplo: verifica duplicata)
    return property_repository.create_property(db=db, property_in=property)


def get_all_property(db: Session):
    return property_repository.get_properties(db)


def get_property_by_id(db: Session, property_id: int):
    db_property = property_repository.get_property_by_id(db, property_id=property_id)
    if db_property is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
    return db_property


def update_existing_property(db: Session, property_id: int, property_in: PropertyUpdate):
    db_property = get_property_by_id(db, property_id)
    return property_repository.update_property(db=db, db_property=db_property, property_in=property_in)


def delete_property_by_id(db: Session, property_id: int):
    db_property = get_property_by_id(db, property_id)
    return property_repository.delete_property(db=db, db_property=db_property)
