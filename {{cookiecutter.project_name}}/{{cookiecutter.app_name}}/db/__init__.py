from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from {{cookiecutter.app_name}}.db import config

uri = config.__baseconfig__[config.ENV]['mysql']['SQLALCHEMY_DATABASE_URI']
# create database
engine = create_engine(uri, echo=False)
# create session using sessionmaker to handle database operation
Session = scoped_session(sessionmaker(bind=engine, autoflush=False))

Base = declarative_base()