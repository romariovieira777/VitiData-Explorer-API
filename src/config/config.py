import os

import pytz
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

SECRET_KEY = "8#y6wf4@t5$s#5r&l#6*kksb(-%omp4gvk(7g73(=pk-h&zjqb"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1h

USERNAME_TMP = "fiap"
PASSWORD_TMP = "fiap"

load_dotenv(find_dotenv())

ENVIRON = os.environ.get('ENVIRON')
TIMEZONE = pytz.timezone(os.environ.get('TIMEZONE'))
HOST_VITI_BRASIL = os.environ.get('HOST_VITI_BRASIL')
PATH_DATABASE_VITIDATA = os.environ.get('PATH_DATABASE_VITIDATA')
ENGINE_VITIDATA = create_engine(f'sqlite:///{PATH_DATABASE_VITIDATA}')
SESSION_VITIDATA = sessionmaker(bind=ENGINE_VITIDATA)
USERNAME_API = os.environ.get('USERNAME_API')
PASSWORD_API = os.environ.get('PASSWORD_API')

Base = declarative_base()


def get_db_vitidata():
    db = SESSION_VITIDATA()
    try:
        yield db
    except Exception as e:
        print(f"Erro durante a transação: {e}")
        db.rollback()
    finally:
        db.close()


ORIGIN_CORS = [
    "*"
]
