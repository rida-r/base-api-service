from fastapi import FastAPI
from app.controllers.sample_db_controller import router as sample_db_controller
from app.database import init_db

app = FastAPI()
app.include_router(sample_db_controller)

@app.on_event("startup")
def on_startup():
    init_db()