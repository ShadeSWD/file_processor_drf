#!/bin/bash

sleep 15

celery -A config worker -l info
