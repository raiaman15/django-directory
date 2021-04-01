#!/bin/sh

echo "CHECKING PORT USAGE"
ss -lntu
echo "COLLECTING STATIC FILES"
python manage.py collectstatic --no-input
exec "$@"