{%- if cookiecutter.api|lower == 'flask' %}
from .namespace1 import main
from .namespace2 import model


__all__ = (
    "main",
    "model",
)
{%- endif %}