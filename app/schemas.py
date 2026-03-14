from pydantic import BaseModel
from datetime import datetime


class KPICreate(BaseModel):
    nombre: str
    descripcion: str | None = None
    meta: float
    periodicidad: str
    responsable: str


class KPIResponse(BaseModel):
    id: int
    nombre: str
    descripcion: str | None
    meta: float
    periodicidad: str
    responsable: str
    fecha_creacion: datetime

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True
