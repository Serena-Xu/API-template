{%- if cookiecutter.api|lower == 'flask' %}
from flask_restx import fields, Model

__all__ = (
    "main_response",
)


main_response = Model('mainArgs', {
    'id': fields.Integer(default=1),
    'name': fields.String(default="TID")
})
{%- endif %}