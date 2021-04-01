#!/bin/sh

# Personal Preference to start fresh - You may comment
# Comment before your first production build (to retain migration history)
# echo "FLUSHING DATABASE"
# python manage.py flush --no-input
# echo "DELETING EXISTING MIGRATION FILES"
# find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
# find . -path "*/migrations/*.pyc"  -delete
# /Personal Preference to start fresh - You may comment

# echo "MAKING MIGRATION FILES"
# python manage.py makemigrations --noinput
echo "MIGRATING DATABASE"
python manage.py migrate --noinput
echo "SEEDING DATABASE | REFRESH"
# python manage.py some_seed
echo "RUNNING ALL TEST CASES"
python manage.py test
echo "STARTING WSGI GUNICORN SERVER WITH 2 WORKERS 4 THREADS (GTHREAD)"
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers=2 --threads=4 --worker-class=gthread