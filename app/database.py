from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

##DA ABASE_URL = "postgresql://postgres:postgres@localhost:5432/kpi_manager"

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
