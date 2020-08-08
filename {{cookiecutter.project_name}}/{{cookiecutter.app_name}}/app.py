# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
{%- if cookiecutter.sqlalchemy|lower == 'y' %}
import logging
import time
{%- endif %}
{%- if cookiecutter.api == 'flask' %}
import flask
from flask import Flask
from flask_restx import Api, Resource
from werkzeug.middleware.proxy_fix import ProxyFix
from {{cookiecutter.app_name}} import apis
from {{cookiecutter.app_name}}.core import parsers, serializers
{%- elif cookiecutter.api == 'fastAPI' %}
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from {{cookiecutter.app_name}} import __version__
from {{cookiecutter.app_name}}.apis import router1
{%- endif %}
{%- if cookiecutter.sqlalchemy|lower == 'y' %}
from sqlalchemy.exc import SQLAlchemyError
{%- endif %}
{%- if cookiecutter.sqlalchemy|lower == 'y' %}
from {{cookiecutter.app_name}}.db import Session, utils as dbutils
{%- endif %}


def create_app():
    {%- if cookiecutter.api == 'flask' %}
    app = Flask(__name__)
    # For HTTPS of serving docs
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)  # type: ignore
    app = Flask(__name__)

    {%- if cookiecutter.sqlalchemy | lower == 'y' %}
    @app.before_request
    def create_session():
        flask.g.session = Session()

    @app.teardown_appcontext
    def shutdown_session(_):
        Session.remove()
    {%-endif %}

    {%- elif cookiecutter.api == 'fastAPI' %}
    app = FastAPI(version=__version__, title="{{cookiecutter.project_name}}",
                  description=f"{{cookiecutter.project_short_description}}")
    app.include_router(router1.main, tags=["main"], prefix="/main")

    {% if cookiecutter.sqlalchemy | lower == 'y' %}
    @app.middleware("http")
    async def db_session_middleware(request: Request, call_next):
        response = Response("Internal server error", status_code=500)
        try:
            request.state.db = Session()
            response = await call_next(request)
        finally:
            request.state.db.close()
        return response
    {%- endif %}
    {%- endif %}

    {% if cookiecutter.sqlalchemy|lower == 'y' %}
    create_db()
    {%- endif %}
    return app

{%- if cookiecutter.api == 'flask' %}
def create_api(app, version, title="title", description="description"):
    api = Api(app, title=title, version=version, description=description)
    api.namespaces.clear()
    for name in apis.__all__:
        endpoint = getattr(apis, name)
        api.add_namespace(endpoint)

    for name in parsers.__all__:
        parser = getattr(parsers, name)
        api.models[parser.name] = parser

    for name in serializers.__all__:
        serializer = getattr(serializers, name)
        api.models[serializer.name] = serializer

    return api
    {%- endif %}

{% if cookiecutter.sqlalchemy|lower == 'y' %}
def create_db():
    num_retries = 0
    max_retries = 3
    while num_retries < max_retries:
        # add foreign keys to sqlite
        try:
            dbutils.create_db()
            break
        except SQLAlchemyError:
            num_retries += 1
            retry_delay = 20
            logging.info(f"Waiting {retry_delay}s to re-connect to mysql...")
            time.sleep(retry_delay)
        if num_retries == max_retries:
            assert False, f"Unable to connect to mysql within {num_retries} attempts"
{%- endif %}