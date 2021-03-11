install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=test.py

lint:
	pylint --disable=R,C source_code_test.py

all: install lint test