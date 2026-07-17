from fastapi import FastAPI

from app.database import init_db
from app.routers import contacts, auth

app = FastAPI()

init_db()

app.include_router(auth.router)
app.include_router(contacts.router)
