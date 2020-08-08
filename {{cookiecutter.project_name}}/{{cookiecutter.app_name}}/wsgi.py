"""Performs config initialization"""
{%- if cookiecutter.api|lower == 'flask' %}
from {{cookiecutter.app_name}}.app import create_app, create_api
from {{cookiecutter.app_name}} import __version__
{% elif cookiecutter.api|lower == 'fastapi' %}
from {{cookiecutter.app_name}}.app import create_app
{%- endif %}
app = create_app()
{%- if cookiecutter.api|lower == 'flask' %}
api = create_api(
    app=app,
    version=__version__,
    title="{{cookiecutter.project_name}}",
    description=f"{{cookiecutter.project_short_description}}"
)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
{%- endif %}