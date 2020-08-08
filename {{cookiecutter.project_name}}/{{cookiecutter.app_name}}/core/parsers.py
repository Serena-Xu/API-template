{%- if cookiecutter.api|lower == 'flask' %}
from flask_restx import fields, Model, reqparse

__all__ = (
    "main_schema",
)

# Schemas (Serializer from Flask Restplus)
main_schema = Model('mainArgs', {
    'id': fields.Integer(required=True, example=1,
                                    description="A short description for name of the model"),
    'name': fields.String(required=True, example="TID_model",
                                    description="A short description for name of the model"),
})

put_args = reqparse.RequestParser()
put_args.add_argument('name', type=str, required=True, help='The name')
{%- endif %}