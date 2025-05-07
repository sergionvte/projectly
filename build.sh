#!/usr/bin/env bash

set -o errexit

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

export PORT=8000
export DJANGO_SETTINGS_MODULE="projectly.settings"
export CLOUD_NAME='dngcfjybb'
export CLOUDINARY_API_KEY='252969854163175'
export CLOUDINARY_API_SECRET='GFD9tlW39PFVkk3LH-_YZN5Gmjo'

python manage.py collectstatic --noinput
python manage.py migrate

python -m daphne -b 0.0.0.0 -p $PORT projectly.asgi:application