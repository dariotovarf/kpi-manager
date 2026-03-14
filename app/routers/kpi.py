from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal
from ..dependencies import get_current_user


router = APIRouter(
    prefix="/kpis",
    tags=["KPIs"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.KPIResponse)
def create_kpi(kpi: schemas.KPICreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    db_kpi = models.KPI(**kpi.dict())
    db.add(db_kpi)
    db.commit()
    db.refresh(db_kpi)
    return db_kpi


@router.get("/", response_model=list[schemas.KPIResponse])
def get_kpis(db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    kpis = db.query(models.KPI).all()
    return kpis

@router.get("/{kpi_id}", response_model=schemas.KPIResponse)
def get_kpi(kpi_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    kpi = db.query(models.KPI).filter(models.KPI.id == kpi_id).first()
    return kpi


@router.put("/{kpi_id}", response_model=schemas.KPIResponse)
def update_kpi(kpi_id: int, kpi_data: schemas.KPICreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    kpi = db.query(models.KPI).filter(models.KPI.id == kpi_id).first()

    if not kpi:
        return {"error": "KPI no encontrado"}

    for key, value in kpi_data.dict().items():
        setattr(kpi, key, value)

    db.commit()
    db.refresh(kpi)

    return kpi


@router.delete("/{kpi_id}")
def delete_kpi(kpi_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    kpi = db.query(models.KPI).filter(models.KPI.id == kpi_id).first()

    if not kpi:
        return {"error": "KPI no encontrado"}

    db.delete(kpi)
    db.commit()

    return {"message": "KPI eliminado"}
