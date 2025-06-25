# main check (Enforced before commit)

format:
    ruff format --preview .

ruff-check:
    ruff check --fix --unsafe-fixes .


basedpyright-check:
    basedpyright .

check: format ruff-check basedpyright-check

test:
    echo "Running tests..."

# Additional analysis checks (not Enforced)

radon:
    radon cc -a -nc -s .

radon-mi:
    radon mi -s .

vulture:
    vulture . --min-confidence 60 --sort-by-size --exclude .venv

check-uv-lock:
    [ -f ./uv.lock ] && uv lock --check || echo "No uv.lock file found, skipping lock check"

compile-user-dep:
    uv pip compile pyproject.toml -o requirements.txt

compile-dev-dep:
    uv pip compile pyproject.toml --all-extras -o requirements-dev.txt

compile-dep: compile-dev-dep check-uv-lock
