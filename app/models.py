from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base


class KPI(Base):
    __tablename__ = "kpis"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)
    meta = Column(Float, nullable=False)
    periodicidad = Column(String)
    responsable = Column(String)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
