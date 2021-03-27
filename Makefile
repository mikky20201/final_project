run:
	FLASK_ENV=development FLASK_APP=games/main.py flask run

test:
	pytest

lint:
	flake8