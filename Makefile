

run:
	python3 app.py

restart: stop run

db-init:
	flask db init

make-initial-migration:
    flask db migrate -m "Initial migration."

make-migration:
	flask db migrate -m "$(m)"

upgrade-db:
	flask db upgrade

downgrade-db:
	flask db downgrade

	