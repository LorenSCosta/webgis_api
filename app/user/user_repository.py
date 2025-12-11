from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.user import user_model

from app.user.user_model import User, UserCreate, UserUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# -----------------------
# SENHA
# -----------------------
def hash_password(password: str) -> str:
    password = password[:72]  # Limite para bcrypt
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)



def get_by_email(db: Session, email: str):
    return db.query(user_model.User).filter(user_model.User.email == email).first()

# -----------------------
# READ
# -----------------------
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session):
    return db.query(User).all()


# -----------------------
# CREATE
# -----------------------
def create_user(db: Session, user_in: UserCreate):
    db_user = User(
        email=user_in.email,
        full_name=user_in.full_name,
        type_user_id=user_in.type_user_id,
        hashed_password=hash_password(user_in.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# -----------------------
# UPDATE
# -----------------------
def update_user(db: Session, db_user: User, user_in: UserUpdate):

    update_data = user_in.model_dump(exclude_unset=True)

    for key, value in update_data.items():

        if key == "password":
            db_user.hashed_password = hash_password(value)

        else:
            setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# -----------------------
# DELETE
# -----------------------
def delete_user(db: Session, db_user: User):
    db.delete(db_user)
    db.commit()
    return db_user

