#!/bin/bash
cd /app/qrqr_backend
pip install django pymysql gunicorn Pillow
cp /app/secret.json /app/qrqr_backend/secret.json
python manage.py migrate
gunicorn --bind 0.0.0.0:8000 config.wsgi:application
python manage.py runserver
