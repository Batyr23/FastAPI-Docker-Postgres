from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Базовая схема для TpDict
class TpDictBase(BaseModel):
    tp_code: int
    tp_name: str
    tp_status: str
    is_commercial: bool
    valid_from: Optional[datetime] = None
    valid_to: Optional[datetime] = None

# Схема для создания новой записи
class TpDictCreate(TpDictBase):
    pass

# Схема для обновления записи
class TpDictUpdate(TpDictBase):
    pass

# Схема для возврата записи
class TpDictOut(TpDictBase):
    id: int

    class Config:
        orm_mode = True
