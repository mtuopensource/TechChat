#!/bin/bash
killall -q python3 || true # XXX: Check if this is safe
cd "$WORKSPACE/backend"
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py test
