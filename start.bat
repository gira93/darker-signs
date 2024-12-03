@echo off
setlocal enabledelayedexpansion

set VENV=venv

if exist %VENV% (
    call %VENV%\Scripts\activate
    python run.py
) else (
    echo Setting up Darker Signs...
    python -m venv %VENV%
    call %VENV%\Scripts\activate
    pip install -r requirements.txt
    pytest tests
    python run.py
)
