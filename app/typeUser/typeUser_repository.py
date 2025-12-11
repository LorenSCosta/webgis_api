from sqlalchemy.orm import Session
from app.typeUser.typeUser_model import TypeUser, TypeUserEnum, TypeUserCreate, TypeUserUpdate


def get_by_tipo(db: Session, tipo: TypeUserEnum):
    return db.query(TypeUser).filter(TypeUser.tipo == tipo).first()


def get_by_id(db: Session, type_id: int):
    return db.query(TypeUser).filter(TypeUser.id == type_id).first()


def get_all(db: Session):
    return db.query(TypeUser).all()


def create(db: Session, type_in: TypeUserCreate):
    db_obj = TypeUser(tipo=type_in.tipo)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


# usado somente pelo seed
def create_from_enum(db: Session, enum_value: TypeUserEnum):
    db_obj = TypeUser(tipo=enum_value)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
