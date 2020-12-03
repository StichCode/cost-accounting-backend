import os

from pydantic import BaseSettings


class Config(BaseSettings):
    SECRET_KEY: str = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI: str = os.environ.get('SQLALCHEMY_DATABASE_URI')


CONFIG = Config()
