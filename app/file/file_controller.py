# app/users/controller.py
from http.client import HTTPException
from fastapi import APIRouter, status
from .file_model import FileCreate, FilePublic, FileUpdate


# 1. Cria um roteador específico para usuários
router = APIRouter(
    prefix="/file",       # Todas as rotas aqui começarão com /users
    tags=["File"]         # Agrupa as rotas no Swagger
)

# Lista FAKE para simular um banco de dados
fake_db = []

# 2. Define o endpoint para criar um usuário
@router.post("/save", response_model=FilePublic)
def create_file(file: FileCreate):
    # user aqui é um objeto Pydantic, com dados já validados!
    new_user_data = file.model_dump()
    new_user_data["id"] = len(fake_db) + 1

    new_file = FilePublic(**new_user_data)
    fake_db.append(new_file)

    return new_file # FastAPI converte para JSON

@router.get("/", response_model=list[FilePublic])
def list_file():
    # Converte os dicionários do 'banco de dados' para o modelo público
    return [FilePublic(**file_data) for file_data in fake_db.values()]

@router.put("/{file_id}", response_model=FilePublic)
def update_file(file_id: int, file_update: FileUpdate):
    if file_id not in fake_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="file not found")

    stored_file_data = fake_db[file_id]
    update_data = file_update.model_dump(exclude_unset=True) # Apenas campos enviados

    updated_file = stored_file_data.copy()
    updated_file.update(update_data)
    fake_db[file_id] = updated_file

    return FilePublic(**updated_file)

@router.delete("/{file_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_file(file_id: int):
    if file_id not in fake_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="file not found")