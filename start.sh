#!/usr/bin/env bash

set -e

VENV="venv"

if [[ -d $VENV ]]; then
	source $VENV/bin/activate
	./run.py
else
	echo "Setting up Darker Signs..."
	python3 -m venv $VENV
	source $VENV/bin/activate
	pip install -r requirements.txt
	pytest ./tests
	./run.py
fi
