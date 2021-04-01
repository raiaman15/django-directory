#!/bin/sh

# Personal Preference to start fresh - You may comment
# Comment before your first production build (to retain migration history)
echo "FLUSHING DATABASE"
python manage.py flush --no-input
echo "DELETING EXISTING MIGRATION FILES"
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
# /Personal Preference to start fresh - You may comment

echo "MAKING MIGRATION FILES"
python manage.py makemigrations --noinput
echo "MIGRATING DATABASE"
python manage.py migrate --noinput
echo "SEEDING DATABASE | REFRESH"
# python manage.py some_seed
echo "RUNNING ALL TEST CASES"
python manage.py test
echo "CREATING TEST SUPERUSER"
echo "from django.contrib.auth import get_user_model; user = get_user_model().objects.create_user(username='admin', email='admin@infroid.com', password='DevTeam@123'); user.is_superuser=True; user.is_staff=True; user.save()" | python manage.py shell

echo "STARTING DJANGO BUILT-IN SERVER"
# SSL Enabled Mode
# python manage.py runserver_plus 0.0.0.0:8000 --cert-file /tmp/cert.crt
# SSL Disabled Mode
python manage.py runserver_plus 0.0.0.0:8000