from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

class pessoa (BaseModel):
    __tablename__ = 'pessoa'
    id = Column(int, primary_key=True) 
    nome = Column(String(100))
    cpf = Column(String(11))
   