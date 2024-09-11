from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .database import Base
from datetime import datetime

# Модель для таблицы tp_dict
class TpDict(Base):
    __tablename__ = 'tp_dict'
    
    tp_code = Column(Integer, primary_key=True, index=True)
    tp_name = Column(String, nullable=False)
    tp_status = Column(String, nullable=False)
    is_commercial = Column(Boolean, default=False)
    valid_from = Column(DateTime, default=datetime.utcnow)
    valid_to = Column(DateTime, nullable=True)
