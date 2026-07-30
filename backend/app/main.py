from fastapi import FastAPI
from app.api import router

APP_VERSION = "0.1.0"

app = FastAPI(title="Demo E-commerce API", version=APP_VERSION)

app.include_router(router)
