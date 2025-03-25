#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

export PORT=8000
export DJANGO_SETTINGS_MODULE="projectly.settings"

python manage.py collectstatic --noinput
python manage.py migrate