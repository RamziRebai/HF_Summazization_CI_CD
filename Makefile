install:
		pip install --upgrade pip &&\
			pip install -r requirements.txt
test:
		python -m pytest -vv -cov=tests tests.py 
lint:
		pylint --disable=R,C app.py
format:
		black *.py
run:	
		python app.py

all:	
		install lint pytest