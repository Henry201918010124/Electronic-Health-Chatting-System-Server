"""
coding:utf-8
file: __init__.py
@time: 2022/12/15 20:21
@desc:
"""
from flask import Flask
from hospital.extensions import db, jwt, cors, migrate
from hospital.api.auth import auth
import click
from hospital.setting import DevelopmentConfig, ProductionConfig
from hospital.database import *
from hospital.api.infos import infos
from hospital.api.post import post_bp
from hospital.api.messages import message
from hospital.api.search import search_bp


def create_app(config=None):
    app = Flask(__name__)
    if config is None:
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(ProductionConfig)
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(auth)
    app.register_blueprint(infos)
    app.register_blueprint(post_bp)
    app.register_blueprint(message)
    app.register_blueprint(search_bp)
    create_command(app)
    return app


def create_command(app: Flask):
    @app.cli.command()
    def initdb():
        db.drop_all()
        click.echo('Drop tables.')
        db.create_all()
        Role.init_data()
        Section.init_data()
        Hospital.init_data()
        User.random_doctor()
        click.echo('Initialized database.')
