#!/bin/bash

sleep 15

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver 0.0.0.0:8000
