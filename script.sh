#!/bin/bash

# Path to the Python script
PYTHON_SCRIPT="PATH TO PY SCRIPT"

# Check if the Python script exists
if [ -f "$PYTHON_SCRIPT" ]; then
    echo "Starting Python script..."
    python3 "$PYTHON_SCRIPT" &
else
    echo "Error: Python script not found at $PYTHON_SCRIPT"
fi

# run this code on terminal to add script to startup: chmod +x /pathToYourScript.sh
