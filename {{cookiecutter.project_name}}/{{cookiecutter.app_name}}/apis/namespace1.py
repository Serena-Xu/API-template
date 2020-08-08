{%- if cookiecutter.api|lower == 'flask' -%}
from flask import request
from flask_restx import Api, Resource, Namespace

from {{cookiecutter.app_name}}.core import serializers, parsers
{%- if cookiecutter.sqlalchemy | lower == 'y' %}
from {{cookiecutter.app_name}}.db import Session, models
{%- endif %}
{%- endif %}

main = Namespace('main', description = 'Main APIs')

@main.route("/")
class MainClass(Resource):
    {%- if cookiecutter.sqlalchemy | lower == 'y' %}
    @main.marshal_with(serializers.main_response, code=200, as_list=True){%- endif %}
    def get(self):
        {%- if cookiecutter.sqlalchemy | lower == 'y' %}
        result = Session.query(models.{{cookiecutter.project_name}}).all()
        {%- else %}
        result = {"Hello": "World"}
        {%- endif %}
        return result

    @main.expect(parsers.main_schema)
    @main.response(200, 'Success.')
    @main.response(500, 'Bad Request.')
    def post(self):
        id = request.json['id']
        name = request.json['name']
        {%- if cookiecutter.sqlalchemy | lower == 'y' %}
        c1 = models.{{cookiecutter.project_name}}(id=id, name=name)
        Session.add(c1)
        Session.flush()
        Session.commit()
        {% else %}
        return {"id": id, "name": name}
        {%- endif %}