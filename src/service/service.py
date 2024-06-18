from datetime import timedelta

from src.config.config import ACCESS_TOKEN_EXPIRE_MINUTES, USERNAME_TMP, PASSWORD_TMP
from src.repository.repository import JWTRepo
from src.schema.schema import LoginSchema


class AuthService:

    @classmethod
    def get_token(cls, request: LoginSchema):

        # Padrão validar usuário na base de dados.

        if request.username == USERNAME_TMP and request.password == PASSWORD_TMP:

            token = JWTRepo.generate_token({
                "username": request.username
            }, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))

            return token
