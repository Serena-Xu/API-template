## Introduction

A template for creating API project. API templates include flask api and fast api. 

flask api: Flask API is a drop-in replacement for Flask that provides an implementation of browsable APIs similar to what Django REST framework provides. It gives you properly content negotiated-responses and smart request parsing. More info see : https://www.flaskapi.org/

fast api: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. More info see: https://fastapi.tiangolo.com/

#

## Prerequsite

#### Install cookiecutter
Make sure you have cookiecutter installed in your local machine.

You can install it using this command : `pip install cookiecutter`

#
#### Create your project

Starting a new project is as easy as running this command at the command line. No need to create a directory first, the cookiecutter will do it for you.

To create a project run the following command and follow the prompt:
````
cookiecutter git@gitlab.beno.ai:bai-utils/templates/flask-template.git
````

### Note
Work directory is: {{project_name}}

#### Install project requirements and run your api
You can install it using pip:
````
cd {{project_name}}
pip install -r {{app_name}}/requirements.txt
./{{app_name}}/run.sh
````
#

### Add your code
If you are using flask, you will need to add code logic into {{app_name}}/apis and {{app_name}}/core.

If you are using fast api, you will need to add code logic into {{app_name}}/apis.

You will see {{app_name}}/db if you choose sqlalchemy is True.

#

### deployment
We use helm chart to deploy {{app_name}} api. For more info about helm chart, please refer to : https://helm.sh/docs/


#
####Use pre-commit to manage and maintain multi-language pre-commit hooks

One-time install::
 1. `pip install pre-commit` or `brew install pre-commit`
 2. A pre-commit configuration file `.pre-commit-config.yaml` has been added to your repo 
 3. Install the git hook scripts `pre-commit install`
 4. You finish all the installation. You can use pre-commit now by `pre-commit run --all-files`
 
 For more details on pre-commit, see https://pre-commit.com/


#
### Maintenance
Email serena.xu@benevolent.ai for questions; open issues, pull requests and modifications as necessary.