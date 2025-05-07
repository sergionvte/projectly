#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

export PORT=8000
export DJANGO_SETTINGS_MODULE="projectly.settings"
export CLOUD_NAME='dngcfjybb'
export CLOUDINARY_API_KEY='252969854163175'
export CLOUDINARY_API_SECRET='GFD9tlW39PFVkk3LH-_YZN5Gmjo'

python3 manage.py collectstatic --noinput
python3 manage.py migrate

python3 -m daphne -b 0.0.0.0 -p $PORT projectly.asgi:application