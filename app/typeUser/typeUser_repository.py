# app/typeUser/typeUser_repository.py

from sqlalchemy.orm import Session
from .typeUser_model import TypeUser, TypeUserCreate, TypeUserUpdate
# =============================
# CREATE
# =============================
def create_type_user(db: Session, type_user: TypeUserCreate):
    """Cria um novo tipo de usuário (admin ou analista)."""
    db_type_user = TypeUser(tipo=type_user.tipo)
    db.add(db_type_user)
    db.commit()
    db.refresh(db_type_user)
    return db_type_user


# =============================
# READ ALL
# =============================
def get_all_type_users(db: Session):
    """Retorna todos os tipos de usuários cadastrados."""
    return db.query(TypeUser).all()


# =============================
# READ BY ID
# =============================
def get_type_user_by_id(db: Session, type_user_id: int):
    """Busca um tipo de usuário pelo ID."""
    return db.query(TypeUser).filter(TypeUser.id == type_user_id).first()


# =============================
# UPDATE
# =============================
def update_type_user(db: Session, db_type_user: TypeUser, type_user_in: TypeUserUpdate):
    """Atualiza os dados de um tipo de usuário existente."""
    update_data = type_user_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_type_user, key, value)

    db.add(db_type_user)
    db.commit()
    db.refresh(db_type_user)
    return db_type_user


# =============================
# DELETE
# =============================
def delete_type_user(db: Session, db_type_user: TypeUser):
    """Deleta um tipo de usuário do banco de dados."""
    db.delete(db_type_user)
    db.commit()
    return db_type_user
