import sqlalchemy
import logging
import flask
from collections import Counter

from functools import wraps
from {{cookiecutter.app_name}}.db import engine, models


class EntryExists(Exception):
    def __init__(self, msg, fields, vals):
        self.msg = msg
        self.duplicated = {f: v for f, v in zip(fields, vals)}

    def __str__(self):
        return f"Duplicated row found for {self.msg} with params: {self.duplicated} already exists"


def create_db():
    logging.info(f"Create db {engine}")
    logging.info("Creating tables")
    models.Base.metadata.create_all(engine)


def clear_db(session):
    logging.info(f"Clear db {session.bind}")
    models.Base.metadata.drop_all(session.bind)


def catch_if_not_in_db(msg):
    def _catch_if_not_in_db(fn):
        @wraps(fn)
        def catch(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except sqlalchemy.orm.exc.NoResultFound:
                flask.abort(404, msg.format(args[1]))

        return catch

    return _catch_if_not_in_db


def list_of_tuples_to_list(input_list):
    return [value for (value,) in input_list]


def raise_if_exists(session, cls, fields, vals):
    assert len(fields) == len(vals)
    cond = (getattr(cls, f) == v for f, v in zip(fields, vals))
    if session.query(sqlalchemy.sql.exists().where(sqlalchemy.and_(*cond))).scalar():
        raise EntryExists(msg=cls.__tablename__, fields=fields, vals=vals)


def get_relation_counts(edges):
    relations = [edge.relation for edge in edges]
    relation_counts = Counter(relations).items()
    return [{"name": name, "count": count} for name, count in relation_counts]
