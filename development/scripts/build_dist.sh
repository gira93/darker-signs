#!/usr/bin/env bash

set -e

if [[ ! -f "requirements.txt" ]]; then
	echo "Error: requirements.txt not found. Please run this script from the project root."
	exit 1
fi

INCLUDE_FILE="packaged.txt"
if [[ ! -f "$INCLUDE_FILE" ]]; then
	echo "Error: $INCLUDE_FILE not found. Please create it with the list of files and directories to package."
	exit 1
fi

COMMIT_HASH=$(git rev-parse --short HEAD 2>/dev/null)
if [[ $? -ne 0 ]]; then
	echo "Error: Not a git repository. Please ensure the project is versioned with Git."
	exit 1
fi

ZIP_FILE="DarkerSigns_vxx_${COMMIT_HASH}_all.zip"

echo "Creating zip file: $ZIP_FILE"
zip -r "$ZIP_FILE" -@ <"$INCLUDE_FILE"

echo "Zip file created successfully: $ZIP_FILE"
