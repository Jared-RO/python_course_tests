#!/bin/bash
# pip install -r requirements.txt

echo "Running quality checks..."

EXIT_STATUS=0
echo "Running BLACK formatter..."
black --config .black.toml . #|| ((EXIT_STATUS++))
git add .
echo "Running PYLINT liniter ..."
pylint --rcfile .pylintrc . #|| ((EXIT_STATUS++))
echo "Running MYPY type checker..."
mypy . --exclude venv || ((EXIT_STATUS++))
echo $EXIT_STATUS
exit $EXIT_STATUS