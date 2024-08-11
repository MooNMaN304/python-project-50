install:
	poetry install

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

build:
	poetry build

publish:
	poetry publish --dry-run

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff
