from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Путь к бд SQLite
DATABASE_URL = "sqlite:///./task_manager.db"

# Создаем движок бд
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Настраиваем сессии для взаимодействия с базой 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей базы 
Base = declarative_base()
