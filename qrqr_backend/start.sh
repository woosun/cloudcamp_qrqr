#!/bin/bash
cd /django/
gunicorn --bind=0.0.0.0:8000 config.wsgi:application