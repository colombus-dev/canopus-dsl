#!/usr/bin/env bash

set -e
set -x

# TODO: type checking currently disabled (because of untyped generated antlr code)
# pyrefly check src/
# pyrefly coverage check src/
ruff check --fix src/
ruff format src/
vulture src/
bandit -r src/
