from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

app = FastAPI()

# Создание всех таблиц в базе данных
models.Base.metadata.create_all(bind=database.engine)

# Корневой маршрут
@app.get("/")
async def root():
    return {"message": "FastAPI CRUD App"}

# Маршрут для создания новой записи
@app.post("/tp_dicts/", response_model=schemas.TpDictCreate)
def create_tp_dict(tp_dict: schemas.TpDictCreate, db: Session = Depends(database.get_db)):
    return crud.create_tp_dict(db=db, tp_dict=tp_dict)

# Маршрут для получения списка записей
@app.get("/tp_dicts/", response_model=list[schemas.TpDictOut])
def read_tp_dicts(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_tp_dicts(db, skip=skip, limit=limit)

# Маршрут для получения одной записи по tp_code
@app.get("/tp_dicts/{tp_code}", response_model=schemas.TpDictOut)
def read_tp_dict(tp_code: int, db: Session = Depends(database.get_db)):
    db_tp_dict = crud.get_tp_dict(db, tp_code=tp_code)
    if db_tp_dict is None:
        raise HTTPException(status_code=404, detail="TpDict not found")
    return db_tp_dict

# Маршрут для обновления записи
@app.put("/tp_dicts/{tp_code}", response_model=schemas.TpDictOut)
def update_tp_dict(tp_code: int, tp_dict: schemas.TpDictUpdate, db: Session = Depends(database.get_db)):
    return crud.update_tp_dict(db=db, tp_code=tp_code, tp_dict=tp_dict)

# Маршрут для удаления записи
@app.delete("/tp_dicts/{tp_code}", response_model=schemas.TpDictOut)
def delete_tp_dict(tp_code: int, db: Session = Depends(database.get_db)):
    return crud.delete_tp_dict(db=db, tp_code=tp_code)
