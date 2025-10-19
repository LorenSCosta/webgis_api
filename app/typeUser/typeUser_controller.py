# app/users/typeUser_controller.py

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from typing import List
from database import SessionLocal
from . import typeUser_service, typeUser_model

router = APIRouter(prefix="/typeUser", tags=["TypeUser"])

# Dependência: cria e fecha sessão do banco automaticamente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =============================
# CREATE
# =============================
@router.post("/save", response_model=typeUser_model.TypeUserPublic, status_code=status.HTTP_201_CREATED)
def create_type_user(typeUser: typeUser_model.TypeUserCreate, db: Session = Depends(get_db)):
    """Cria um novo tipo de usuário (admin ou analista)."""
    return typeUser_service.create_new_type_user(db=db, typeUser=typeUser)

# =============================
# READ ALL
# =============================
@router.get("/", response_model=List[typeUser_model.TypeUserPublic])
def read_type_users(db: Session = Depends(get_db)):
    """Lista todos os tipos de usuários."""
    return typeUser_service.get_all_type_users(db)

# =============================
# READ BY ID
# =============================
@router.get("/{typeUser_id}", response_model=typeUser_model.TypeUserPublic)
def read_type_user(typeUser_id: int, db: Session = Depends(get_db)):
    """Busca um tipo de usuário pelo ID."""
    return typeUser_service.get_type_user_by_id(db, typeUser_id=typeUser_id)

# =============================
# UPDATE
# =============================
@router.put("/{typeUser_id}", response_model=typeUser_model.TypeUserPublic)
def update_type_user(typeUser_id: int, typeUser: typeUser_model.TypeUserUpdate, db: Session = Depends(get_db)):
    """Atualiza um tipo de usuário existente."""
    return typeUser_service.update_existing_type_user(db=db, typeUser_id=typeUser_id, typeUser_in=typeUser)

# =============================
# DELETE
# =============================
@router.delete("/{typeUser_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_type_user(typeUser_id: int, db: Session = Depends(get_db)):
    """Deleta um tipo de usuário pelo ID."""
    typeUser_service.delete_type_user_by_id(db=db, typeUser_id=typeUser_id)
    return None
