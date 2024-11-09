.PHONY: init run f

init:
	pip install -r requirements.txt

run:
	python3 main.py

# フォーマッター
f:
	autoflake --remove-all-unused-imports -r --in-place . --exclude=venv
	isort .
	black .