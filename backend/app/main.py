from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Demo E-commerce API")

app.include_router(router)
