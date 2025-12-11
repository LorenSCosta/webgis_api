from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List


from app.database import get_db
from app.typeUser.typeUser_model import TypeUserPublic, TypeUserCreate, TypeUserUpdate
from app.typeUser import typeUser_service

router = APIRouter(prefix="/type-user", tags=["TypeUser"])

@router.post("/", response_model=TypeUserPublic, status_code=status.HTTP_201_CREATED)
def create_type_user(type_in: TypeUserCreate, db: Session = Depends(get_db)):
    return typeUser_service.create_type_user(db, type_in)

@router.get("/", response_model=List[TypeUserPublic])
def list_type_users(db: Session = Depends(get_db)):
    return typeUser_service.get_all_types(db)

@router.get("/{type_id}", response_model=TypeUserPublic)
def get_type_user(type_id: int, db: Session = Depends(get_db)):
    return typeUser_service.get_type_by_id(db, type_id)


