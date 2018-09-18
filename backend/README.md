# TechChat Backend
[![Build Status](http://heroku-badge.herokuapp.com/?app=open-source-at-mtu-tech-chat&root=api/&style=flat)](https://open-source-at-mtu-tech-chat.herokuapp.com/web/)

## Table of Contents
 - [Getting started](#getting-started)
 - [Deploying](#deploying-with-jenkins)

## Getting started
1.  Clone this repository: `git clone https://github.com/mtuopensource/TechChat.git`
2.  Open a terminal and navigate to the backend directory
3.  Run `pip install -r requirements.txt`
4.  Run `py manage.py runserver`

## Unit Tests
1.  Clone this repository: `git clone https://github.com/mtuopensource/TechChat.git`
2.  Open a terminal and navigate to the backend directory
3.  Run `py manage.py test api.tests`

## Heroku
Heroku is a free hosting service for small projects. Easily setup and deploy from the command line via Git.
### Buildpacks:
1.  `heroku buildpacks:clear` 
2.  `heroku buildpacks:set https://github.com/timanovsky/subdir-heroku-buildpack` 
3.  `heroku buildpacks:add heroku/python` 
### Environment Variables:
1.  `heroku config:set PROJECT_PATH='backend'` 
2.  `heroku config:set DISABLE_COLLECTSTATIC=1` 
3.  `heroku config:set DJANGO_SETTINGS_MODULE='common.settings'`
4.  `heroku config:set ENCODING='utf-8'`
5.  `heroku config:set DJANGO_SETTINGS_MODULE='mongodb://user:password@localhost/db?authSource=tech_chat'`
### Deployment
1. Deploy from the Heroku web interface
3. Run `heroku ps:scale web=1`  
