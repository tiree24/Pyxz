release: python manage.py migrate 
release: python manage.py createsuperuser -h admin1 --email a@a.com 
release: password 
release: password
web: gunicorn --env DJANGO_SETTINGS_MODULE=pyxz.settings pyxz.wsgi