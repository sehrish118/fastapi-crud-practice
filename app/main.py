from fastapi import FastAPI

from database import init_db
from routers import contacts

app = FastAPI()

init_db()

app.include_router(contacts.router)
