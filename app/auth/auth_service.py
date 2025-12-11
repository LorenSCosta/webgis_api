from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.typeUser.typeUser_model import TypeUser
from app.user import user_repository
from app.user.user_model import User
from app.auth.auth_schema import RegisterDto
from app.user.user_model import  User
# -------------------------------
# Configurações JWT e bcrypt
# -------------------------------
SECRET_KEY = "sua-chave-secreta-super-dificil"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# -------------------------------
# Funções de senha
# -------------------------------
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se a senha em texto puro bate com o hash do banco"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Gera hash bcrypt para uma senha"""
    return pwd_context.hash(password)

# -------------------------------
# Função de token JWT
# -------------------------------
def create_access_token(data: dict):
    """Gera token JWT válido por ACCESS_TOKEN_EXPIRE_MINUTES"""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# -------------------------------
# Função de autenticação
# -------------------------------
def authenticate_user(db: Session, email: str, password: str):
    """Autentica usuário pelo email e senha"""
    user = user_repository.get_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def register_user(data: RegisterDto, db: Session):
    hashed_password = user_repository.hash_password(data.password)

    # Se enviou type_user_id, usa ele; senão, usa padrão "viewer" ou "analista"
    if data.type_user_id:
        type_user = db.query(TypeUser).filter(TypeUser.id == data.type_user_id).first()
        if not type_user:
            raise HTTPException(status_code=400, detail="Tipo de usuário inválido")
    else:
        type_user = db.query(TypeUser).filter(TypeUser.tipo == "viewer").first()
        if not type_user:
            raise HTTPException(status_code=500, detail="Tipo de usuário padrão não encontrado")

    # Cria usuário
    new_user = User(
        full_name=data.full_name,
        email=data.email,
        hashed_password=hashed_password,
        type_user=type_user
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

