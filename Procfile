web: gunicorn FindIt.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
heroku ps:scale web=1
web: python myServer.py