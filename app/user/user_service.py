from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.user import user_repository, user_model

# -------------------------------
# CRUD de usuários
# -------------------------------

def create_new_user(db: Session, user_in: user_model.UserCreate):
    """Cria um novo usuário, verificando duplicidade de email"""
    existing_user = user_repository.get_by_email(db, user_in.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )
    return user_repository.create_user(db, user_in)

def get_user_by_email(db: Session, email: str):
    """Retorna usuário pelo email"""
    return user_repository.get_by_email(db, email)

def get_all_users(db: Session):
    """Lista todos os usuários"""
    return user_repository.get_users(db)

def get_user_by_id(db: Session, user_id: int):
    """Retorna usuário pelo ID"""
    user = user_repository.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
    return user

def update_existing_user(db: Session, user_id: int, user_in: user_model.UserUpdate):
    """Atualiza usuário existente"""
    db_user = get_user_by_id(db, user_id)
    return user_repository.update_user(db, db_user, user_in)

def delete_user_by_id(db: Session, user_id: int):
    """Deleta usuário existente"""
    db_user = get_user_by_id(db, user_id)
    return user_repository.delete_user(db, db_user)
