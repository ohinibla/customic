#!/bin/bash
set -e  

python customic/manage.py makemigrations
python customic/manage.py migrate
python customic/manage.py spectacular --color --file schema.yml
python customic/manage.py collectstatic --noinput
python customic/manage.py create_user

exec python customic/manage.py runserver 0.0.0.0:8000
