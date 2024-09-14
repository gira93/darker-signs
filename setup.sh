#!/usr/bin/env bash

set -e

VENV="venv"

if [[ ! -d $VENV ]]; then
	echo "Setting up Darker Signs..."
	python3 -m venv $VENV
	source $VENV/bin/activate
	pip install -r requirements.txt
	pytest ./tests
	echo "All good!, use ./start.sh to run"
fi
