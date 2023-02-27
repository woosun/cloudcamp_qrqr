#!/bin/bash

sudo apt update -y
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt install python3.9

pip3 install -r requirements.txt
gunicorn --bind=0.0.0.0:8000 config.wsgi:application