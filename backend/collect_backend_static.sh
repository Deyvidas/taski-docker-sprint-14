python manage.py migrate
rm -r /app/collected_static
python manage.py collectstatic
cp -r /app/collected_static/* /taski_backend_static/static
gunicorn --bind 0.0.0.0:8000 backend.wsgi