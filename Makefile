.PHONY: install test lint type-check build generate clean help

## install: Install package in editable mode with dev dependencies
install:
	pip install -e ".[dev]"

## test: Run pytest with coverage
test:
	python -m pytest --cov=graphiant_sdk --cov-report=term --cov-report=xml

## lint: Run flake8 on hand-written files only (generated files excluded via .flake8)
lint:
	flake8 graphiant_cli/ \
	  graphiant_sdk/api_client.py \
	  graphiant_sdk/configuration.py \
	  graphiant_sdk/exceptions.py \
	  graphiant_sdk/rest.py \
	  graphiant_sdk/api_response.py \
	  tests/

## type-check: Run mypy (generated models excluded via pyproject.toml)
type-check:
	mypy graphiant_sdk/ graphiant_cli/

## build: Build wheel and source distribution
build:
	python -m build

## generate: Regenerate SDK from the OpenAPI spec
generate:
	@bash scripts/generate.sh

## clean: Remove build artifacts
clean:
	rm -rf dist/ build/ *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true

## help: Show this help
help:
	@grep -E '^## ' Makefile | sed 's/## /  /'

.DEFAULT_GOAL := test
