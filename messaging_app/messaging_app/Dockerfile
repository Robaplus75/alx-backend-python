FROM python:3.10

WORKDIR /app

COPY ./requirements.txt .
RUN apt update
RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential pkg-config
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt
RUN pip install gunicorn

COPY . .

EXPOSE 8000
# -p
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "messaging_app.wsgi:application"]
