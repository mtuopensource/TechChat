import requests
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.test import Client
from api.views.BoardViewSet import BoardViewSet
from django.template.loader import render_to_string

def index(request):
    client = Client()
    response = client.post('/api/users/login/', {'email': 'ajwalhof@mtu.edu', 'password': 'test'})
    response = client.get('/api/boards/', {})
    boards = json.loads(response.content.decode('utf-8'))

    rendered = render_to_string('index.html', {'boards': boards})
    return HttpResponse(rendered)

def board(request, id):
    client = Client()
    response = client.post('/api/users/login/', {'email': 'ajwalhof@mtu.edu', 'password': 'test'})
    response = client.get('/api/boards/', {})
    boards = json.loads(response.content.decode('utf-8'))
    response = client.get('/api/boards/' + id + '/', {})
    board = json.loads(response.content.decode('utf-8'))
    rendered = render_to_string('board.html', {'board': board, 'boards': boards})
    return HttpResponse(rendered)

def thread(request, id):
    client = Client()
    response = client.post('/api/users/login/', {'email': 'ajwalhof@mtu.edu', 'password': 'test'})
    response = client.get('/api/boards/', {})
    boards = json.loads(response.content.decode('utf-8'))
    response = client.get('/api/threads/' + id + '/', {})
    thread = json.loads(response.content.decode('utf-8'))
    rendered = render_to_string('thread.html', {'thread': thread, 'boards': boards})
    return HttpResponse(rendered)

def createthread(request):
    client = Client()
    response = client.post('/api/users/login/', {'email': 'ajwalhof@mtu.edu', 'password': 'test'})
    response = client.get('/api/boards/', {})
    boards = json.loads(response.content.decode('utf-8'))
    if request.method == "POST":
        board = request.POST.get('board')
        title = request.POST.get('title')
        ttext = request.POST.get('content')
        response = client.post('/api/threads/', {
            'board': board,
            'title': title,
            'content': ttext
        })
        if response.status_code == 201:
            id = json.loads(response.content.decode('utf-8')).get('id')
            return redirect('/web/thread/' + id + '/')
    return render(request, 'thread-create.html', {'boards': boards})
