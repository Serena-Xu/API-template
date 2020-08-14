install:
	pip install -r requirements.txt


tests:
	pip install -r tests/requirements.txt
	pytest tests/


start-server: install
	./{{cookiecutter.app_name}}/run.sh
