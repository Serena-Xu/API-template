from typing import List
from fastapi import APIRouter
from http import HTTPStatus
{%- if cookiecutter.sqlalchemy | lower == 'y' %}
from {{cookiecutter.app_name}}.db import models, schemas, Session
{%- endif %}

main = APIRouter()

@main.get('/', response_model=List[schemas.Main])
def get():
    {%- if cookiecutter.sqlalchemy | lower == 'y' %}
    result = Session.query(models.{{cookiecutter.project_name}}).all()
    {%- else %}
    result = {"Hello": "World"}
    {%- endif %}
    return result

@main.post('/', response_model=schemas.Main, status_code=HTTPStatus.CREATED)
def post(id: int, name: str):
        {%- if cookiecutter.sqlalchemy | lower == 'y' %}
        c1 = models.{{cookiecutter.project_name}}(id=id, name=name)
        Session.add(c1)
        Session.flush()
        Session.commit()
        {% else %}
        return {"id": id, "name": name}
        {%- endif %}
