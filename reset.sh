#!/usr/bin/env bash

set -e

VENV="venv"

echo "Resetting Darker Signs..."
rm -r $VENV
rm -r rootfs

echo "Done, start again with ./start.sh"
