#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

# Ensure staticfiles directory exists and is in the right place
mkdir -p staticfiles
python manage.py collectstatic --no-input --clear

# List what was collected for debugging
ls -la staticfiles/
