FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -U pip setuptools && \
    pip install gunicorn==20.1.0 && \
    pip install -r requirements.txt --no-cache-dir

RUN chmod +x collect_backend_static.sh

CMD /app/collect_backend_static.sh