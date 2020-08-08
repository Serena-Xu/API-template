{%- if cookiecutter.api|lower == 'flask' %}
from flask_restx import Api, Resource, Namespace

from {{cookiecutter.app_name}}.core import serializers, parsers
{%- if cookiecutter.sqlalchemy | lower == 'y' %}
from {{cookiecutter.app_name}}.db import Session, models
{%- endif %}
{%- endif %}

model = Namespace('model', description = 'Another APIs')

@model.route("/<int:id>")
@model.param('id', 'The id')
@model.response(200, 'Success')
@model.response(500, 'ServerError')
class Main(Resource):
    {%- if cookiecutter.sqlalchemy | lower == 'y' %}
    def delete(self, id):
        result = Session.query(models.{{cookiecutter.project_name}}).filter(models.{{cookiecutter.project_name}}.id == id).one()
        Session.delete(result)
        Session.commit()
        {%- endif %}

    @model.expect(parsers.put_args)
    def put(self, id):
        args = parsers.put_args.parse_args()
        {%- if cookiecutter.sqlalchemy | lower == 'y' %}
        Session.query(models.{{cookiecutter.project_name}}).filter(models.{{cookiecutter.project_name}}.id == id).update(
            {"name": args.name})
        {%- endif %}
        return {"id": id, "name": args.name}