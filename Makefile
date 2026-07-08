.PHONY: all lint typecheck test test-quick test-api test-appium clean venv help

PYTHON    := python3
PIP       := $(PYTHON) -m pip
PYTEST    := $(PYTHON) -m pytest
RUFF      := $(PYTHON) -m ruff
BLACK     := $(PYTHON) -m black
MYPY      := $(PYTHON) -m mypy

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

all: lint typecheck test-quick ## Run all checks (lint + typecheck + quick tests)

venv: ## Create virtual environment and install dependencies
	$(PYTHON) -m venv venv
	. venv/bin/activate && $(PIP) install -r automation/requirements.txt

lint: ## Run Ruff linter and Black format check
	$(RUFF) check automation/ manual-tests/
	$(BLACK) --check --diff automation/

format: ## Auto-format with Black
	$(BLACK) automation/

typecheck: ## Run MyPy type checking
	$(MYPY) automation/

test: ## Run all tests (excluding Appium)
	$(PYTEST) automation/tests/ -m "not appium" -v

test-quick: ## Run fast unit/smoke tests only
	$(PYTEST) automation/tests/ -m "not appium and not integration" -v

test-api: ## Run arXiv API integration tests
	$(PYTEST) automation/tests/ -m "integration" -v

test-appium: ## Run Appium UI smoke tests (requires device/emulator)
	$(PYTEST) automation/tests/appium/ -m appium -v

test-cov: ## Run tests with coverage report
	$(PYTEST) automation/tests/ -m "not appium" --cov=automation --cov-report=term-missing -v

clean: ## Remove caches and build artifacts
	rm -rf .ruff_cache .mypy_cache .pytest_cache
	rm -rf __pycache__ */__pycache__ */*/__pycache__
	rm -rf test-results coverage.xml .coverage htmlcov
	rm -rf .eggs *.egg-info build dist
