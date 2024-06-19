import json
from datetime import timedelta
from io import StringIO
from typing import Any

import requests
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.config.config import ACCESS_TOKEN_EXPIRE_MINUTES, USERNAME_TMP, PASSWORD_TMP, HOST_VITI_BRASIL, \
    PATH_DATABASE_VITIDATA, ENGINE_VITIDATA, get_db_vitidata
from src.model.model import User
from src.repository.repository import JWTRepo, UserRepository
from src.schema.schema import LoginSchema


class AuthService:

    @classmethod
    def get_token(cls, request: LoginSchema):

        session = next(get_db_vitidata())

        user = UserRepository.retrieve_by_first_username(session, User, request.username)

        if user is not None:

            if UserRepository.verify_password(request.password, user.hashed_password):

                if request.username == USERNAME_TMP and request.password == PASSWORD_TMP:
                    token = JWTRepo.generate_token({
                        "username": request.username
                    }, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))

                    return token
            else:
                raise Exception("Incorrect username or password")


class VitiEmbrapaService:

    def __init__(self, host: str):
        self.host = host
        self.header = {
            'Accept': 'application/json',
            'Content-Type': 'text/csv'
        }

    def download(self, param: str):
        response = requests.get(f'{self.host}/{param}', data=None, headers=self.header)

        return response.text

    def update_bd(self, data: str, table_name: str):
        df = pd.read_csv(StringIO(data), delimiter=';')

        df.to_sql(table_name, con=ENGINE_VITIDATA, if_exists='replace', index=False)


class ProductionService:

    @staticmethod
    def update_table_production():
        viti = VitiEmbrapaService(host=HOST_VITI_BRASIL)
        data = viti.download(param="download/Producao.csv")
        viti.update_bd(data=data, table_name="producao")
