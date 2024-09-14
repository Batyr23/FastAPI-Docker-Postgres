from sqlalchemy.orm import Session
from . import models, schemas

# SELECT записи по tp_code
def get_tp_dict(db: Session, tp_code: int):
    return db.query(models.TpDict).filter(models.TpDict.tp_code == tp_code).first()

# SELECT всех записей с возможностью пропуска и лимита
def get_tp_dicts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TpDict).offset(skip).limit(limit).all()

# Create новой записи
def create_tp_dict(db: Session, tp_dict: schemas.TpDictCreate):
    db_tp_dict = models.TpDict(**tp_dict.dict())
    db.add(db_tp_dict)
    db.commit()
    db.refresh(db_tp_dict)
    return db_tp_dict

# Delete записи по tp_code
def delete_tp_dict(db: Session, tp_code: int):
    db_tp_dict = db.query(models.TpDict).filter(models.TpDict.tp_code == tp_code).first()
    if db_tp_dict:
        db.delete(db_tp_dict)
        db.commit()
    return db_tp_dict

# Update записи по tp_code
def update_tp_dict(db: Session, tp_code: int, tp_dict: schemas.TpDictUpdate):
    db_tp_dict = db.query(models.TpDict).filter(models.TpDict.tp_code == tp_code).first()
    if db_tp_dict:
        for key, value in tp_dict.dict().items():
            setattr(db_tp_dict, key, value)
        db.commit()
        db.refresh(db_tp_dict)
    return db_tp_dict

#--------------------------------------------------------------------------------------
# Создание нового клиента
def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# Получение клиента по ID
def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

# Получение всех клиентов с возможностью пропуска и лимита
def get_customers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Customer).offset(skip).limit(limit).all()

# Обновление клиента
def update_customer(db: Session, customer_id: int, customer: schemas.CustomerUpdate):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if db_customer:
        for key, value in customer.dict(exclude_unset=True).items():
            setattr(db_customer, key, value)
        db.commit()
        db.refresh(db_customer)
    return db_customer

# Удаление клиента
def delete_customer(db: Session, customer_id: int):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if db_customer:
        db.delete(db_customer)
        db.commit()
    return db_customer