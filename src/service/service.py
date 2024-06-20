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

"""
    Authentication
"""


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


"""
    Viti Embrapa
"""


class VitiEmbrapaService:

    def __init__(self, host: str):
        self.host = host
        self.header = {
            'Accept': 'application/json',
            'Content-Type': 'text/csv'
        }

    def identify_delimiter(self, data: str):
        delimiters = [',', ';', '\t']
        lines = data.strip().split('\n')
        header = lines[0]
        for delimiter in delimiters:
            if header.count(delimiter) > 0:
                return delimiter
        return None

    def download(self, param: str):
        response = requests.get(f'{self.host}/{param}', data=None, headers=self.header)

        response.encoding = 'utf-8'

        return response.text

    def update_bd(self, data: str, table_name: str):

        delimiter = self.identify_delimiter(data)

        if not delimiter:
            raise ValueError("Unable to identify delimiter")

        df = pd.read_csv(StringIO(data), encoding='utf-8', delimiter=delimiter)

        df.to_sql(table_name, con=ENGINE_VITIDATA, if_exists='replace', index=False)


"""
    Production
"""


class ProductionService:

    @staticmethod
    def update_table_production():
        viti = VitiEmbrapaService(host=HOST_VITI_BRASIL)
        data = viti.download(param="download/Producao.csv")
        viti.update_bd(data=data, table_name="producao")


"""
    Commercialization
"""


class CommercializationService:

    @staticmethod
    def update_table_commercialization():
        viti = VitiEmbrapaService(host=HOST_VITI_BRASIL)
        data = viti.download(param="download/Comercio.csv")
        viti.update_bd(data=data, table_name="comercializacao")


"""
    Export
"""


class ExportWineService:

    @staticmethod
    def update_table_exp_wine():
        viti = VitiEmbrapaService(host=HOST_VITI_BRASIL)
        data = viti.download(param="download/ExpVinho.csv")
        viti.update_bd(data=data, table_name="exportacao_vinhos")


class ExportSparklingService:

    @staticmethod
    def update_table_exp_sparkling():
        viti = VitiEmbrapaService(host=HOST_VITI_BRASIL)
        data = viti.download(param="download/ExpEspumantes.csv")
        viti.update_bd(data=data, table_name="exportacao_espumantes")


class ExportGrapeService:

    @staticmethod
    def update_table_exp_grape():
        viti = VitiEmbrapaService(host=HOST_VITI_BRASIL)
        data = viti.download(param="download/ExpUva.csv")
        viti.update_bd(data=data, table_name="exportacao_uvas_frescas")


class ExportJuiceService:

    @staticmethod
    def update_table_exp_juice():
        viti = VitiEmbrapaService(host=HOST_VITI_BRASIL)
        data = viti.download(param="download/ExpSuco.csv")
        viti.update_bd(data=data, table_name="exportacao_sucos")


"""
    Import
"""


class ImportWineService:

    @staticmethod
    def update_table_imp_wine():
        viti = VitiEmbrapaService(host=HOST_VITI_BRASIL)
        data = viti.download(param="download/ImpVinhos.csv")
        viti.update_bd(data=data, table_name="importacao_vinhos")


class ImportSparklingService:

    @staticmethod
    def update_table_imp_sparkling():
        viti = VitiEmbrapaService(host=HOST_VITI_BRASIL)
        data = viti.download(param="download/ImpEspumantes.csv")
        viti.update_bd(data=data, table_name="importacao_espumantes")


class ImportFreshGrapeService:

    @staticmethod
    def update_table_imp_fresh_grapes():
        viti = VitiEmbrapaService(host=HOST_VITI_BRASIL)
        data = viti.download(param="download/ImpFrescas.csv")
        viti.update_bd(data=data, table_name="importacao_uvas_frescas")


class ImportDriedGrapesService:

    @staticmethod
    def update_table_imp_dried_grapes():
        viti = VitiEmbrapaService(host=HOST_VITI_BRASIL)
        data = viti.download(param="download/ImpPassas.csv")
        viti.update_bd(data=data, table_name="importacao_uvas_passas")


class ImportJuiceService:

    @staticmethod
    def update_table_imp_juice():
        viti = VitiEmbrapaService(host=HOST_VITI_BRASIL)
        data = viti.download(param="download/ImpSuco.csv")
        viti.update_bd(data=data, table_name="importacao_sucos")


"""
    Processing
"""


class ProcessingViniferasService:

    @staticmethod
    def update_table_process_viniferas():
        viti = VitiEmbrapaService(host=HOST_VITI_BRASIL)
        data = viti.download(param="download/ProcessaViniferas.csv")
        viti.update_bd(data=data, table_name="processamento_viniferas")


class ProcessingAmericanAndHybridService:

    @staticmethod
    def update_table_process_american_and_hybrid():
        viti = VitiEmbrapaService(host=HOST_VITI_BRASIL)
        data = viti.download(param="download/ProcessaAmericanas.csv")
        viti.update_bd(data=data, table_name="processamento_americanas_hibridas")


class ProcessingTableGrapesService:

    @staticmethod
    def update_table_process_table_grapes():
        viti = VitiEmbrapaService(host=HOST_VITI_BRASIL)
        data = viti.download(param="download/ProcessaMesa.csv")
        viti.update_bd(data=data, table_name="processamento_uvas_mesa")


class ProcessingClassLessService:

    @staticmethod
    def update_table_process_class_less():
        viti = VitiEmbrapaService(host=HOST_VITI_BRASIL)
        data = viti.download(param="download/ProcessaSemclass.csv")
        viti.update_bd(data=data, table_name="processamento_sem_classe")
