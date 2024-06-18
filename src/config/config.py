import os

import pytz
from dotenv import load_dotenv, find_dotenv

SECRET_KEY = "8#y6wf4@t5$s#5r&l#6*kksb(-%omp4gvk(7g73(=pk-h&zjqb"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 # 1h

USERNAME_TMP = "fiap"
PASSWORD_TMP = "fiap"


load_dotenv(find_dotenv())

ENVIRON = os.environ.get('ENVIRON')
TIMEZONE = pytz.timezone(os.environ.get('TIMEZONE'))


ORIGIN_CORS = [
    "*"
]
