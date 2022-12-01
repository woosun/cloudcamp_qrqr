FROM python:3.9.15
ADD ./qrqr_backend /app
COPY /SSD_DATA/django/secret.json /app/secret.json
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]