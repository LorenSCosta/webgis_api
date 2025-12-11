from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.auth.auth_schema import RegisterDto
from app.database import get_db
from app.auth import auth_service
from app.auth.auth_service import create_access_token, register_user  # use o nome correto



router = APIRouter(prefix="/auth", tags=["Authentication"])

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = auth_service.authenticate_user(db, data.email, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    
    access_token = auth_service.create_access_token({"sub": str(user.id)})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_type": user.type_user.tipo  # usa apenas type_user
    }




@router.post("/register")
def register(data: RegisterDto, db: Session = Depends(get_db)):
    print("Recebido full_name:", data.full_name)
    user = register_user(data, db)
    print("Salvando full_name:", user.full_name)
    return user
