from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

from app.typeUser.typeUser_model import TypeUserPublic


# ==============================================================
# SQLALCHEMY MODEL (TABELA)
# ==============================================================

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    
    # Chave estrangeira → type_users.id
    type_user_id = Column(Integer, ForeignKey("type_users.id"), nullable=False)

    # Relacionamento ORM
    type_user = relationship("TypeUser", back_populates="users")


# ==============================================================
# Pydantic Schemas
# ==============================================================

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str | None = Field(default=None, min_length=3)
    type_user_id: int


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = Field(default=None, min_length=8)
    full_name: str | None = Field(default=None, min_length=3)
    type_user_id: int | None = None


class UserPublic(BaseModel):
    id: int
    email: EmailStr
    full_name: str | None = None
    type_user: TypeUserPublic

    class Config:
        from_attributes = True
