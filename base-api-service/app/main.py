from fastapi import FastAPI
from app.controllers.balance_sheet_controller import router as balance_sheet_router
from app.database import init_db

app = FastAPI()
app = FastAPI()
app.include_router(balance_sheet_router)
@app.on_event("startup")
def on_startup():
    init_db()