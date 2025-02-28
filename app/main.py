from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.endpoints import auth, users, predictions
from app.db.session import engine
from sqlmodel import SQLModel

app = FastAPI(title="FastAPI Boilerplate")

app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
app.include_router(users.router, prefix="/api/v1", tags=["users"])