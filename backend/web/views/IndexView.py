import requests
import json
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.test import Client
from api.views.BoardViewSet import BoardViewSet

def index(request):
    client = Client()
    response = client.post('/api/users/login/', {'email': 'ajwalhof@mtu.edu', 'password': 'test'})
    response = client.get('/api/boards/', {})
    boards = json.loads(response.content)

    rendered = render_to_string('index.html', {'boards': boards})
    return HttpResponse(rendered)

def board(request, id):
    client = Client()
    response = client.post('/api/users/login/', {'email': 'ajwalhof@mtu.edu', 'password': 'test'})
    response = client.get('/api/boards/', {})
    boards = json.loads(response.content)
    response = client.get('/api/boards/' + id + '/', {})
    threads = json.loads(response.content)

    rendered = render_to_string('board.html', {'threads': threads, 'boards': boards})
    return HttpResponse(rendered)
