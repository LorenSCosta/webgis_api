from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.typeUser import typeUser_repository
from app.typeUser.typeUser_model import TypeUserCreate, TypeUserUpdate, TypeUserEnum


def create_type_user(db: Session, type_in: TypeUserCreate):

    # Verifica se já existe
    exists = typeUser_repository.get_by_tipo(db, type_in.tipo)
    if exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="TypeUser already exists"
        )

    return typeUser_repository.create(db, type_in)


def get_all_types(db: Session):
    return typeUser_repository.get_all(db)


def get_type_by_id(db: Session, type_id: int):
    obj = typeUser_repository.get_by_id(db, type_id)

    if not obj:
        raise HTTPException(status_code=404, detail="TypeUser not found")

    return obj

