from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings  # Используем переменные окружения

# Строка подключения к базе данных теперь берется из переменных окружения
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Создание сессии для базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
