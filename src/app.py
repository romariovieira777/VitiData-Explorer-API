from typing import Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from model.model import User
from src.config.config import ORIGIN_CORS, ENGINE_VITIDATA, Base, USERNAME_API, PASSWORD_API
from src.router.router import router
from passlib.context import CryptContext


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGIN_CORS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def initialize_db():
    Base.metadata.create_all(bind=ENGINE_VITIDATA)

def get_password_hash(password):
    return pwd_context.hash(password)

def add_user(username: str, password: str):
    with ENGINE_VITIDATA.connect() as connection:
        hashed_password = get_password_hash(password)
        insert_query = User.__table__.insert().values(username=username, hashed_password=hashed_password)
        connection.execute(insert_query)

@app.on_event("startup")
async def startup_event():
    initialize_db()
    add_user(USERNAME_API, PASSWORD_API)

@app.get("/")
def root() -> Any:
    return {"message": "Welcome to VitiData Explorer API | FIAP"}


app.include_router(router=router)
