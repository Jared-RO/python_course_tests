#!/bin/bash
# pip install -r requirements.txt

black --config .black.toml .
pylint --rcfile .pylintrc .
mypy . --exclude venv