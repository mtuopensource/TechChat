#!/bin/bash
cd "$WORKSPACE/backend"
pip3 install -r requirements.txt
python3.6 manage.py migrate
python3.6 manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1 &
