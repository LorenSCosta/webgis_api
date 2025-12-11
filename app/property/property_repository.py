from sqlalchemy.orm import Session
from app.property.property_model import Property, PropertyCreate, PropertyUpdate


# READ
def get_property_by_id(db: Session, property_id: int):
    return db.query(Property).filter(Property.id == property_id).first()


def get_property_by_owner(db: Session, owner: str):
    return db.query(Property).filter(Property.owner == owner).first()


def get_properties(db: Session):
    return db.query(Property).all()


# CREATE
def create_property(db: Session, property_in: PropertyCreate):
    db_property = Property(
        farm_name=property_in.farm_name,
        owner=property_in.owner,
        area_ha=property_in.area_ha,
        latitude=property_in.latitude,
        longitude=property_in.longitude,
        city=property_in.city,
    )
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property


# UPDATE
def update_property(db: Session, db_property: Property, property_in: PropertyUpdate):
    update_data = property_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_property, field, value)

    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property


# DELETE
def delete_property(db: Session, db_property: Property):
    db.delete(db_property)
    db.commit()
    return db_property
