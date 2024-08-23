install:
	poetry install

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest tests/json_flat.py

test-coverage:
	poetry run pytest tests/json_flat.py --cov=gendiff --cov-report xml
	poetry run pytest tests/json_flat.py --cov

check:
	poetry run flake8 gendiff
	poetry run flake8 tests
	poetry run pytest tests/json_flat.py
