FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r /app/requirements.txt --no-cache-dir

CMD gunicorn --bind 0.0.0.0:8000 backend.wsgi