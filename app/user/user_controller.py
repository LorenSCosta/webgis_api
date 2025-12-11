from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from fastapi.responses import Response
from sqlalchemy.orm import Session
from app.database import get_db
from app.user import user_service, user_model

router = APIRouter(prefix="/user", tags=["Users"])

# -------------------------------
# Endpoints CRUD de usuário
# -------------------------------

@router.post("/", response_model=user_model.UserPublic, status_code=status.HTTP_201_CREATED)
def create_user(user_in: user_model.UserCreate, db: Session = Depends(get_db)):
    """Cria um novo usuário"""
    return user_service.create_new_user(db, user_in)

@router.get("/", response_model=List[user_model.UserPublic])
def read_users(db: Session = Depends(get_db)):
    """Lista todos os usuários"""
    return user_service.get_all_users(db)

@router.get("/{user_id}", response_model=user_model.UserPublic)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """Busca usuário por ID"""
    return user_service.get_user_by_id(db, user_id)

@router.put("/{user_id}", response_model=user_model.UserPublic)
def update_user(user_id: int, user_in: user_model.UserUpdate, db: Session = Depends(get_db)):
    """Atualiza usuário por ID"""
    return user_service.update_existing_user(db, user_id, user_in)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Deleta usuário por ID"""
    user_service.delete_user_by_id(db, user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
