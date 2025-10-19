# app/typeUser/typeUser_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from . import typeUser_model, typeUser_repository


# =============================
# CREATE
# =============================
def create_new_type_user(db: Session, type_user: typeUser_model.TypeUserCreate):
    """Cria um novo tipo de usuário (admin ou analista)."""
    return typeUser_repository.create_type_user(db=db, type_user=type_user)


# =============================
# READ ALL
# =============================
def get_all_type_users(db: Session):
    """Lista todos os tipos de usuários."""
    return typeUser_repository.get_all_type_users(db)


# =============================
# READ BY ID
# =============================
def get_type_user_by_id(db: Session, type_user_id: int):
    """Busca um tipo de usuário pelo ID, com tratamento de erro."""
    db_type_user = typeUser_repository.get_type_user_by_id(db, type_user_id=type_user_id)
    if db_type_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Type user not found"
        )
    return db_type_user


# =============================
# UPDATE
# =============================
def update_existing_type_user(db: Session, type_user_id: int, type_user_in: typeUser_model.TypeUserUpdate):
    """Atualiza um tipo de usuário existente."""
    db_type_user = get_type_user_by_id(db, type_user_id)
    return typeUser_repository.update_type_user(db=db, db_type_user=db_type_user, type_user_in=type_user_in)


# =============================
# DELETE
# =============================
def delete_type_user_by_id(db: Session, type_user_id: int):
    """Deleta um tipo de usuário existente."""
    db_type_user = get_type_user_by_id(db, type_user_id)
    return typeUser_repository.delete_type_user(db=db, db_type_user=db_type_user)
