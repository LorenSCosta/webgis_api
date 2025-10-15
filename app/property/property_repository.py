from sqlalchemy.orm import Session
from app.property import property_model




# --- FUNÇÕES DE LEITURA (READ) ---
def get_property_by_id(db: Session, property_id: int):
    """
    Busca um único usuário pelo seu ID.
    """
    return db.query(property_model.Property).filter(property_model.Property.id == property_id).first()


def get_property_by_owner(db: Session, owner: str):
    """Busca um único usuário pelo seu nome."""
    return db.query(property_model.Property).filter(property_model.Property.owner == owner).first()

def get_property(db: Session):
    """
    Busca todos os proprietarios cadastrados no banco de dados.
    .all(): Retorna uma lista com todos os resultados da consulta.
    """
    return db.query(property_model.Property).all()

# --- FUNÇÕES DE CRIAÇÃO (CREATE) ---
def create_property(db: Session, property: property_model.PropertyCreate):
    """
    Cria um novo usuário no banco de dados.
    """
    db_property = property_model.Property(farm_name=property.farm_name, owner=property.owner, area_ha=property.area_ha,
                                     latitude=property.latitude, longitude=property.longitude, city=property.city)
    
    db.add(db_property)      # Adiciona o novo objeto à sessão (área de preparação).
    db.commit()         # Salva (commita) as mudanças no banco de dados.
    db.refresh(db_property) # Atualiza o objeto db_user com os dados do banco (como o ID gerado).
    return db_property


# --- FUNÇÃO DE ATUALIZAÇÃO (UPDATE) ---
def update_property(db: Session, db_property: property_model.Property, property_in: property_model.PropertyUpdate):
    """Atualiza os dados de um usuário existente."""
    update_data = property_in.model_dump(exclude_unset=True) # Pega só os campos que foram enviados na requisição.
    for field, value in update_data.items():
        setattr(db_property, field, value) # Atualiza o atributo do objeto com o novo valor.

    db.add(db_property) # Adiciona o objeto modificado à sessão.
    db.commit()     # Salva as alterações.
    db.refresh(db_property) # Atualiza o objeto com os dados do banco.
    return db_property

# --- FUNÇÃO DE DELEÇÃO (DELETE) ---
def delete_property(db: Session, db_property: property_model.Property):
    """Deleta um usuário do banco de dados."""
    db.delete(db_property) # Marca o objeto para deleção.
    db.commit()        # Efetiva a deleção no banco.
    return db_property


