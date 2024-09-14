#!/usr/bin/env bash

VENV="venv"

if [[ -d $VENV ]]; then
	source $VENV/bin/activate
	./run.py
else
	echo "Run ./setup.sh first!"
fi
