{%- if cookiecutter.api|lower == 'fastapi' %}
uvicorn {{cookiecutter.app_name}}.wsgi:app --host 0.0.0.0 --port 8080
{%- elif cookiecutter.api|lower == 'flask'%}
TIMEOUT=10000

gunicorn \
    -b 0.0.0.0:8080 \
    -t $TIMEOUT \
    -k gevent --worker-connections 10 \
    --keep-alive 3600 \
    --log-level info \
    {{cookiecutter.app_name}}.wsgi:app

{%- endif %}

