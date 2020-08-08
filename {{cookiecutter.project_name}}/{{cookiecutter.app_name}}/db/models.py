from {{cookiecutter.app_name}}.db import Base
from sqlalchemy import Column, Integer, String

__all__ = (
    "{{cookiecutter.project_name}}",
)

class {{cookiecutter.project_name}}(Base):
    __tablename__ = "{{cookiecutter.project_name}}"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=20))
