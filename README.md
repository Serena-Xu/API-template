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

In deployment, it uses api chart (version: 1.1.9) lives in https://chartmuseum.stbl.svc.int.beno.ai. It contains 1 deployment, 1 service and 1 ingress. 

Project contains a .gitlab-ci.yaml would you deploy {{app_name}} api into gitops cluster.


***Note*** : 
- Make sure you update `image` and `imageTag` in `k8s/gitops/{{cookiecutter.app_name}}-hr.yaml` file
- Update git user email and git name in `fetch_gitops_repo` in `.gitlab-ci.yaml`
- Update api host name `external-dns.alpha.kubernetes.io/hostname` and `hosts` to your host in {{cookiecutter.app_name}}-hr.yaml,


### Maintenance
Email serena.xu@benevolent.ai for questions; open issues, pull requests and modifications as necessary.