#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

export PORT=8000
export DJANGO_SETTINGS_MODULE="projectly.settings"
export CLOUD_NAME='dngcfjybb'
export CLOUDINARY_API_KEY='252969854163175'
export CLOUDINARY_API_SECRET='GFD9tlW39PFVkk3LH-_YZN5Gmjo'
export RENDER=True
export DATABASE_URL='postgresql://sergionvte:ipe6jw0KnpvWRO5L33UAByOTcpmVtdSa@dpg-d0e1ts8dl3ps73b91cdg-a/projectly'

python manage.py collectstatic --noinput