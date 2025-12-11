from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Float
from app.database import Base



class Property(Base):
    __tablename__ = "property"  # manter se preferir; poderia ser "properties"

    id = Column(Integer, primary_key=True, index=True)
    farm_name = Column(String, index=True)
    owner = Column(String, index=True)
    area_ha = Column(Float, index=True)
    latitude = Column(String, index=True)
    longitude = Column(String, index=True)
    city = Column(String, index=True)


# ---------------------------
# Schemas Pydantic (request/response)
# ---------------------------
class PropertyCreate(BaseModel):
    farm_name: str | None = Field(default=None, min_length=3)
    owner: str | None = Field(default=None, min_length=3)
    area_ha: float | None = Field(default=None)
    latitude: str | None = Field(default=None, min_length=3)
    longitude: str | None = Field(default=None, min_length=3)
    city: str | None = Field(default=None, min_length=3)


class PropertyUpdate(BaseModel):
    farm_name: str | None = Field(default=None, min_length=3)
    owner: str | None = Field(default=None, min_length=3)
    area_ha: float | None = Field(default=None)
    latitude: str | None = Field(default=None, min_length=3)
    longitude: str | None = Field(default=None, min_length=3)
    city: str | None = Field(default=None, min_length=3)


class PropertyPublic(BaseModel):
    id: int
    farm_name: str | None
    owner: str | None
    area_ha: float | None
    latitude: str | None
    longitude: str | None
    city: str | None

    class Config:
        from_attributes = True
