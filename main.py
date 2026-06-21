
from fastapi import FastAPI
from app.api.webhook import router

app = FastAPI(
    title="TV MT5 Executor"
)

app.include_router(router)
