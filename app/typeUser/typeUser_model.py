from pydantic import BaseModel
from sqlalchemy import Column, Enum, Integer, String
from database import Base
import enum
from sqlalchemy.orm import relationship

# ==================================
# ENUM: tipos de usuário fixos
# ==================================

class TypeUserEnum(str, enum.Enum):
    admin = "admin"
    analista = "analista"


# ==================================
# MODEL: tabela no banco (opcional)
# ==================================

class TypeUser(Base):
    __tablename__ = "type_users"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(Enum(TypeUserEnum), nullable=False, unique=True)  # admin ou analista


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
        from_attributes = True  # permite converter de SQLAlchemy para Pydantic

users = relationship("User", back_populates="type_user")