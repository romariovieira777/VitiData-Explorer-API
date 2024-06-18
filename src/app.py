from typing import Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.config import ORIGIN_CORS
from src.router.router import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGIN_CORS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)


@app.get("/")
def root() -> Any:
    return {"message": "VitiData Explorer API | FIAP"}


app.include_router(router=router)
