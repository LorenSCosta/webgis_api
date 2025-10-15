
from sqlalchemy import Column, Enum, Integer, String
from database import Base
import enum

# ==================================

class TypeUserEnum(str, enum.Enum):
    admin = "admin"
    analista = "analista"


class typeUser(Base):
    __tablename__ = "type_users"

    id = Column(Integer, primary_key=True, index=True)    
    tipo = Column(Enum (TypeUserEnum), nullable=False)  # admin ou analista
    