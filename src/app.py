from typing import Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model.model import User
from src.config.config import ORIGIN_CORS, ENGINE_VITIDATA, Base, USERNAME_API, PASSWORD_API, get_db_vitidata
from src.repository.repository import UserRepository
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
    session = next(get_db_vitidata())

    try:
        hashed_password = get_password_hash(password)

        user = UserRepository.retrieve_by_first_username(session, User, username)

        if user is None:
            new_user = User(username=username, hashed_password=hashed_password)
            UserRepository.insert(session, new_user)

    except Exception as e:
        print(f"[+] Failed to add user: {e}")
    finally:
        session.close()


@app.on_event("startup")
async def startup_event():
    initialize_db()
    add_user(USERNAME_API, PASSWORD_API)


@app.get("/")
def root() -> Any:
    return {"message": "Welcome to VitiData Explorer API | FIAP"}


app.include_router(router=router)
