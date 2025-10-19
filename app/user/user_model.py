# app/users/models.py
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from app.typeUser.typeUser_model import TypeUserEnum

# ==================================
# MODELO DA TABELA (SQLAlchemy)
# ==================================
class User(Base):
    __tablename__ = "users"

    # Colunas da tabela
    id: int = Column(Integer, primary_key=True, index=True)
    email: str = Column(String, unique=True, index=True, nullable=False)
    hashed_password: str = Column(String, nullable=False)
    full_name: str | None = Column(String, index=True, nullable=True)

    # Relacionamento com TypeUser
    type_user_id: int = Column(Integer, ForeignKey("type_users.id"), nullable=False)
    type_user = relationship("TypeUser", back_populates="users")  # Nome da classe SQLAlchemy lá no outro arquivo


# ==================================
# SCHEMAS (Pydantic)
# ==================================

# 🔹 Schema para criação
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str | None = Field(default=None, min_length=3)
    type_user_id: int  # FK para TypeUser


# 🔹 Schema para atualização
class UserUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = Field(default=None, min_length=8)
    full_name: str | None = Field(default=None, min_length=3)
    type_user_id: int | None = None


# 🔹 Schema de resposta pública
class UserPublic(BaseModel):
    id: int
    email: EmailStr
    full_name: str | None = None
    type_user: TypeUserEnum

    class Config:
        from_attributes = True  # Permite converter objetos ORM → Pydantic
