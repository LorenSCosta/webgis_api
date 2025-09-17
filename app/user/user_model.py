# app/users/models.py
from pydantic import BaseModel, EmailStr, Field
from app.person.person_model import PersonBase

# Schema para criação
class UserCreate(PersonBase):
    password: str = Field(min_length=8)
    

# Schema para ATUALIZAR um usuário
# Todos os campos são opcionais
class UserUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = Field(default=None, min_length=8)
    full_name: str | None = Field(default=None, min_length=3)

# Schema para retornar API ao cliente
class UserPublic(PersonBase):
    id: int
