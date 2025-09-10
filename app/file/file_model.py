# app/file/file_model.py
from pydantic import BaseModel, EmailStr, Field

# Schema para d
class FileCreate(BaseModel):
    nome: str = Field(min_length=5)
    formato: str
    caminho: str

# Schema para os dados que o cliente envia ao ATUALIZAR um usuário
# Todos os campos são opcionais
class FileUpdate(BaseModel):
    id: int
    nome: str | None = None
    formato: str | None = Field(default=None, min_length=8)
    caminho: str | None = Field(default=None, min_length=3)

# Schema para os dados que a API retorna ao cliente
class FilePublic(BaseModel):
    id: int
    nome: str
    formato: str
    caminho: str