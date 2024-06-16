import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

ENVIRON = os.environ.get('ENVIRON')
TIMEZONE = os.environ.get('TIMEZONE')

ORIGIN_CORS = [
    "*"
]
