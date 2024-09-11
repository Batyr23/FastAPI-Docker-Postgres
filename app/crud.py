from sqlalchemy.orm import Session
from . import models, schemas

# Получение записи по tp_code
def get_tp_dict(db: Session, tp_code: int):
    return db.query(models.TpDict).filter(models.TpDict.tp_code == tp_code).first()

# Получение всех записей с возможностью пропуска и лимита
def get_tp_dicts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TpDict).offset(skip).limit(limit).all()

# Создание новой записи
def create_tp_dict(db: Session, tp_dict: schemas.TpDictCreate):
    db_tp_dict = models.TpDict(**tp_dict.dict())
    db.add(db_tp_dict)
    db.commit()
    db.refresh(db_tp_dict)
    return db_tp_dict

# Удаление записи по tp_code
def delete_tp_dict(db: Session, tp_code: int):
    db_tp_dict = db.query(models.TpDict).filter(models.TpDict.tp_code == tp_code).first()
    if db_tp_dict:
        db.delete(db_tp_dict)
        db.commit()
    return db_tp_dict

# Обновление записи по tp_code
def update_tp_dict(db: Session, tp_code: int, tp_dict: schemas.TpDictUpdate):
    db_tp_dict = db.query(models.TpDict).filter(models.TpDict.tp_code == tp_code).first()
    if db_tp_dict:
        for key, value in tp_dict.dict().items():
            setattr(db_tp_dict, key, value)
        db.commit()
        db.refresh(db_tp_dict)
    return db_tp_dict
