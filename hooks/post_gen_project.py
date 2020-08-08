#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Post gen hook to ensure that the generated project
has only one package management, either pipenv or pip."""
import os
import logging
import shutil

LOGGER = logging.getLogger()

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

if __name__ == "__main__":
    if 'n' in '{{ cookiecutter.sqlalchemy|lower }}':
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, '{{cookiecutter.app_name}}', 'db'))
        os.remove(os.path.join(PROJECT_DIRECTORY, '{{cookiecutter.app_name}}', 'config', 'config.yaml'))
    if 'flask' in '{{ cookiecutter.api|lower }}':
        app_dir = os.path.join(PROJECT_DIRECTORY, '{{cookiecutter.app_name}}')
        files_to_remove = [os.path.join(app_dir, 'apis/router1.py')]
        for file in files_to_remove:
            os.remove(file)
    if 'fastapi' in '{{ cookiecutter.api|lower }}':
        app_dir = os.path.join(PROJECT_DIRECTORY, '{{cookiecutter.app_name}}')
        files_to_remove = [os.path.join(app_dir, 'apis/namespace1.py'),
                           os.path.join(app_dir, 'apis/namespace2.py'),
                           os.path.join(app_dir, 'apis/__init__.py')]
        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, '{{cookiecutter.app_name}}', 'core'))
