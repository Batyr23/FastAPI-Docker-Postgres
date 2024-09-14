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
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

#----------------------------------------------------------------------
# Базовая схема клиента

class CustomerBase(BaseModel):
    name: str
    phone_number: str
    email: Optional[str] = None
    address: Optional[str] = None

# Схема для создания нового клиента
class CustomerCreate(CustomerBase):
    pass

# Схема для обновления клиента
class CustomerUpdate(CustomerBase):
    pass

# Схема для возврата клиента
class CustomerOut(CustomerBase):
    id: int
    registration_date: Optional[str]  # Добавьте соответствующие поля
    is_active: Optional[bool]

    class Config:
        orm_mode = True