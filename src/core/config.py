from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.models import Base

DATABASE_URL = "postgresql://hrd_user:hrd2024@localhost/hrd"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)