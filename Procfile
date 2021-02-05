release: python manage.py migrate aulas --noinput
release: python manage.py loaddata aulas/fixtures/fixtures.json --noinput
release: python manage.py migrate --noinput
web: gunicorn portal_ensino.wsgi --log-file -
