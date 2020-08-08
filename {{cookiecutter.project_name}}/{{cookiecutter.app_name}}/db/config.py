{%- if cookiecutter.sqlalchemy|lower == 'y' %}
import os
import yaml

CONFIG_FILE = os.environ.get('CONFIG_FILE', 'config.yaml')
ENV = os.environ.get('ENV', 'local')

dirname = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(dirname, CONFIG_FILE)

__baseconfig__ = yaml.load(open(CONFIG_PATH))
mysql_config = __baseconfig__[ENV]['mysql']

if ENV == "local":
    __baseconfig__[ENV]['mysql']['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.dirname(dirname)}/sqlite.db'
else:
    __baseconfig__[ENV]['mysql']['SQLALCHEMY_DATABASE_URI'] = (
        'mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}'.format(
            user=mysql_config['user'],
            password=mysql_config['password'],
            host=mysql_config['host'],
            port=mysql_config['port'],
            dbname=mysql_config['dbname'],
        )
    )
{%- endif %}
