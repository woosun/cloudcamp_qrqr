FROM python:3.9.15
ADD ./ /app
COPY /SSD_DATA/secret.json /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]