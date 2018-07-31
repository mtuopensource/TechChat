#!/bin/bash
killall -q python3.6 || true
cd "$WORKSPACE/backend"
pip3 install --user -r requirements.txt
rm .env || true
echo "HOST=mongodb://user:pass@localhost/db?authSource=authDb" >> .env
echo "ENCODING=utf-8" >> .env
python3.6 manage.py migrate
python3.6 manage.py test
