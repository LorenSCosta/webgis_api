from pydantic import BaseModel
from sqlalchemy import Column, Enum, Integer
from sqlalchemy.orm import relationship
from app.database import Base

import enum

# ===============================
# ENUM DEFINITIVO
# ===============================
class TypeUserEnum(str, enum.Enum):
    admin = "admin"
    analista = "analista"
    viewer = "viewer"


# ===============================
# MODEL SQLALCHEMY
# ===============================
class TypeUser(Base):
    __tablename__ = "type_users"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(Enum(TypeUserEnum), nullable=False, unique=True)

    users = relationship("User", back_populates="type_user")


# ==================================
# SCHEMAS (Pydantic)
# ==================================

class TypeUserBase(BaseModel):
    tipo: TypeUserEnum


class TypeUserCreate(TypeUserBase):
    """Schema para criação de um tipo de usuário"""
    pass


class TypeUserUpdate(BaseModel):
    """Schema para atualização de tipo de usuário"""
    tipo: TypeUserEnum | None = None


class TypeUserPublic(TypeUserBase):
    """Schema para retorno ao cliente"""
    id: int

    class Config:
        from_attributes = True

users = relationship("User", back_populates="type_user")