from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from .database import Base
from datetime import datetime

class TpDict(Base):
    __tablename__ = 'tp_dict'

    id = Column(Integer, primary_key=True, index=True)
    tp_code = Column(Integer, unique=True, index=True)
    tp_name = Column(String, nullable=False)
    tp_status = Column(String, nullable=False)
    is_commercial = Column(Boolean, default=False)
    valid_from = Column(DateTime, default=datetime.utcnow)
    valid_to = Column(DateTime, nullable=True)
    
    # log data
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
