from fastapi import FastAPI
from .database import engine
from . import models
from .routers import kpi

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(kpi.router)


@app.get("/")
def read_root():
    return {"message": "KPI Manager API is running 🚀"}
