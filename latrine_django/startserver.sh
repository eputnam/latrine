python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixturefile.json
python manage.py get_restrooms
uwsgi --chdir=./ --module=latrine_django.wsgi:application --env DJANGO_SETTINGS_MODULE=latrine_django.settings --socket=/tmp/latrine_django.sock --master --http :8000
