from sqlalchemy.orm import Session
from fastapi import HTTPException, status


from app.property import property_repository
from . import property_model

def create_new_property(db: Session, property: property_model.PropertyCreate):
    return property_repository.create_property(db=db, property=property)

def get_all_property(db: Session):
    """Serviço para listar todos os proprietários. Neste caso, apenas repassa a chamada."""
    return property_repository.get_property(db)

def get_property_by_id(db: Session, property_id: int):
    """Serviço para buscar um proprietário pelo ID, com tratamento de erro."""
    db_property = property_repository.get_property_by_id(db, property_id=property_id)
    # REGRA DE NEGÓCIO: Se o proprietário não for encontrado, retornar um erro 404.
    if db_property is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
    return db_property

def update_existing_property(db: Session, property_id: int, property_in: property_model.PropertyUpdate):
    """Serviço para atualizar um usuário, com tratamento de erro."""
    db_property = get_property_by_id(db, property_id) # Reutiliza a lógica para buscar e checar se o proprietário existe.
    return property_repository.update_property(db=db, db_property=db_property, property_in=property_in)

def delete_property_by_id(db: Session, property_id: int):
    """Serviço para deletar um usuário, com tratamento de erro."""
    db_property = get_property_by_id(db, property_id) # Reutiliza a lógica para buscar e checar se o proprietário existe.
    return property_repository.delete_property(db=db, db_property=db_property)
