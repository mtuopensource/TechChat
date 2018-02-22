## Table of Contents
 - [Getting started](#getting-started)
 - [Deploying](#deploying)

## Getting started
1.  Clone this repository: `git clone https://github.com/mtuopensource/TechChat.git`
2.  Open a terminal and navigate to the backend directory
3.  Run `pip install -r requirements.txt`
4.  Run `py manage.py runserver`

## Unit Tests
1.  Clone this repository: `git clone https://github.com/mtuopensource/TechChat.git`
2.  Open a terminal and navigate to the backend directory
3.  Run `py manage.py test api.tests`

## Deploying with Jenkins
Create a build shell script with the following lines:
1.  `killall -q python3 || true`
2.  `cd "/var/lib/jenkins/workspace/TechChat Backend/backend"`
3.  `pip3 install -r requirements.txt`
4.  `python3 manage.py test`

Create a post build shell script with the following lines:
1.  `pip install -r requirements.txt` 
2.  `py manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1 &`
