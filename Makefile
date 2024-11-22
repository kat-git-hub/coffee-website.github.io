install:
	poetry install
lint:
	poetry run flake8 app.py
runserver:
	poetry run python run.py
migrate:
	poetry run python app.py migrate
migrations:
	poetry run python app.py makemigrations