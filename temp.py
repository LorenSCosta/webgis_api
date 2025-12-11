from sqlalchemy.orm import Session
from app.database import get_db
from app.user.user_model import User
from app.auth.auth_service import verify_password


def test_user_password(email: str, senha_fornecida: str):
    # Criar sessão do banco
    db: Session = next(get_db())
    
    # Buscar usuário pelo email
    user = db.query(User).filter(User.email == email).first()
    
    if not user:
        print(f"Usuário com email '{email}' não encontrado.")
        return
    
    # Verificar senha
    if verify_password(senha_fornecida, user.hashed_password):
        print("Senha correta!")
    else:
        print("Senha incorreta!")

if __name__ == "__main__":
    # Alterar email e senha para testar
    email_teste = "user4@example.com"
    senha_teste = "123456789"
    
    test_user_password(email_teste, senha_teste)
