"""
coding:utf-8
file: setting.py
@time: 2020/11/26 21:46
@desc:
"""
import os
from dotenv import load_dotenv
import sys
import datetime

WIN = sys.platform.startswith('win')
if WIN:
    sqlite_pre = 'sqlite:///'
else:
    sqlite_pre = 'sqlite:////'

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
load_dotenv('.env')


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # database config
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_PWD = os.getenv('DATABASE_PWD')
    DATABASE_HOST = os.getenv('DATABASE_HOST')
    DATABASE_PORT = os.getenv('DATABASE_PORT')
    DATABASE_NAME = os.getenv('DATABASE_NAME')

    UPLOAD_PATH = os.path.join(basedir, 'assets')
    AVATARS_SAVE_PATH = UPLOAD_PATH + '/avatars/'

    # jwt config
    JWT_SECRET_KEY = 'a3e847bc-5707-11ec-9608-9f9d60f7ad70'
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=30)
    JWT_TOKEN_LOCATION = ['cookies', 'headers', 'json', 'query_string']
    JWT_HEADER_NAME = 'Access-Token'
    JWT_ACCESS_COOKIE_NAME = 'Access-Token'
    JWT_QUERY_STRING_NAME = 'access_token'


class DevelopmentConfig(BaseConfig):
    if BaseConfig.DATABASE_USER is not None:
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8mb4'.format(BaseConfig.DATABASE_USER,
                                                                                       BaseConfig.DATABASE_PWD,
                                                                                       BaseConfig.DATABASE_HOST,
                                                                                       BaseConfig.DATABASE_NAME)
    else:
        SQLALCHEMY_DATABASE_URI = sqlite_pre + os.path.join(basedir, 'data.db')
    REDIS_URL = "redis://localhost:6379"


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8mb4'.format(BaseConfig.DATABASE_USER,
                                                                                   BaseConfig.DATABASE_PWD,
                                                                                   BaseConfig.DATABASE_HOST,
                                                                                   BaseConfig.DATABASE_NAME)
    REDIS_URL = "redis://localhost:6379"
