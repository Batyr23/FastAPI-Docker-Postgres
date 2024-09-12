from fastapi import FastAPI, Request, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from . import crud, models, schemas, database

app = FastAPI()

# Jinja2
templates = Jinja2Templates(directory="templates")

# Creation Tables in Database
models.Base.metadata.create_all(bind=database.engine)

# Root path for index.html
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Обработка формы для добавления записи через данные формы
@app.post("/add/")
async def add_tp_dict(
    tp_code: int = Form(...),
    tp_name: str = Form(...),
    tp_status: str = Form(...),
    is_commercial: bool = Form(...),
    valid_from: str = Form(...),
    valid_to: str = Form(...),
    db: Session = Depends(database.get_db)
):
    tp_dict_data = schemas.TpDictCreate(
        tp_code=tp_code,
        tp_name=tp_name,
        tp_status=tp_status,
        is_commercial=is_commercial,
        valid_from=valid_from,
        valid_to=valid_to
    )
    crud.create_tp_dict(db=db, tp_dict=tp_dict_data)
    return RedirectResponse("/", status_code=303)

# Просмотр всех записей с поддержкой удаления и обновления
@app.get("/tp_dicts_view/")
async def read_tp_dicts_view(request: Request, db: Session = Depends(database.get_db)):
    tp_dicts = crud.get_tp_dicts(db)
    return templates.TemplateResponse("tp_dicts.html", {"request": request, "tp_dicts": tp_dicts})

# Обработка удаления записи
@app.post("/delete/{tp_code}")
async def delete_tp_dict_view(tp_code: int, db: Session = Depends(database.get_db)):
    crud.delete_tp_dict(db=db, tp_code=tp_code)
    return RedirectResponse("/tp_dicts_view", status_code=303)

# Обработка обновления записи через JSON & application/x-www-form-urlencoded
@app.post("/update/{tp_code}")
async def update_tp_dict_view(
    tp_code: int,
    tp_name: str = Form(...),
    tp_status: str = Form(...),
    is_commercial: bool = Form(...),
    valid_from: str = Form(...),
    valid_to: str = Form(...),
    db: Session = Depends(database.get_db)
):
    tp_dict_data = schemas.TpDictUpdate(
        tp_code=tp_code,
        tp_name=tp_name,
        tp_status=tp_status,
        is_commercial=is_commercial,
        valid_from=valid_from,
        valid_to=valid_to
    )
    crud.update_tp_dict(db=db, tp_code=tp_code, tp_dict=tp_dict_data)
    return RedirectResponse("/tp_dicts_view", status_code=303)