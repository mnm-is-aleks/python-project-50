install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

check:
	 make lint
	 make test

test:
	 poetry run pytest

test-coverage:
	 poetry run pytest --cov=gendiff --cov-report=xml:coverage/coverage.xml


.PHONY: install build publish lint
