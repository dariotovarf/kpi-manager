from fastapi import FastAPI
from .database import engine
from . import models
from .routers import kpi
from .routers import users

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(kpi.router)
app.include_router(users.router)


@app.get("/")
def read_root():
    return {"message": "KPI Manager API is running 🚀"}
