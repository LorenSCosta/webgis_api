# app/property/property_model.py
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Float
from database import Base



class Property(Base):
    __tablename__ = "property"  # Nome da tabela no banco

    # Colunas da tabela
    id = Column(Integer, primary_key=True, index=True)
    farm_name = Column(String, index=True) 
    owner = Column(String, index=True)
    area_ha = Column(Float, index=True,) 
    latitude = Column(String, index=True) 
    longitude = Column(String, index=True) 
    city = Column(String, index=True) 


# Schema para os dados que o cliente envia ao CRIAR um usuário
class PropertyCreate(BaseModel):

    farm_name: str | None = Field(default= None, min_length=3)
    owner: str | None = Field(default= None, min_length=3)
    area_ha: float | None = Field(default= None)
    latitude: str | None = Field(default= None, min_length=3)
    longitude: str | None = Field(default= None, min_length=3)
    city: str | None = Field(default= None, min_length=3)

   


# Schema para os dados que o cliente envia ao ATUALIZAR um usuário
class PropertyUpdate(BaseModel):
    farm_name: str | None = Field(default=None, min_length=3)
    owner: str | None = Field(default=None, min_length=3)
    area_ha: float | None = Field(default=None)
    latitude: str | None = Field(default=None, min_length=3)
    longitude: str | None = Field(default=None, min_length=3)
    city: str | None = Field(default=None, min_length=3)

# Schema para os dados que a API RETORNA ao cliente (público)
# NUNCA inclua a senha ou outros dados sensíveis aqui!
class PropertyPublic(BaseModel):
    id: int
    farm_name: str
    owner: str
    area_ha: float
    latitude: str
    longitude: str
    city: str

    class Config:
        orm_mode = True  # Necessário para trabalhar com ORM do SQLAlchemy
