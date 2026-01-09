lint:
	uv run ruff check .
	uv run mypy src/

format:
	uv run ruff format .

test:
	uv run pytest -q

run:
	uv run src/DuskHollow.py