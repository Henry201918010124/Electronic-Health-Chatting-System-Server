"""
coding:utf-8
file: extensions.py
@time: 2022/12/15 20:15
@desc:
"""
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

jwt = JWTManager()
db = SQLAlchemy()
cors = CORS()
migrate = Migrate()

