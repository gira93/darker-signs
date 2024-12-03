@echo off
setlocal

set VENV=venv

echo Resetting Darker Signs...
if exist %VENV% (
    rmdir /s /q %VENV%
)
if exist rootfs (
    rmdir /s /q rootfs
)

echo Done, start again with start.bat
