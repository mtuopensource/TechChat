import requests
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.test import Client
from api.views.BoardViewSet import BoardViewSet
from api.response import SUCCESS
from django.template.loader import render_to_string

from .Helper import *

@check_authentication
def index(request, client=None):
    boards_list = get_boards_list(client)
    return render(request, 'index.html', {
        'boards_list': boards_list
    })

@check_authentication
def board(request, id, client=None):
    board       = get_board      (client, id)
    boards_list = get_boards_list(client)
    return render(request, 'board.html', {
        'board':       board,
        'boards_list': boards_list
    })

def login(request):
    if request.method == "POST":
        c = Client()
        username = request.POST.get('username')
        password = request.POST.get('password')
        response = c.post('/api/users/login/', {'email': username, 'password': password})
        if response.status_code == SUCCESS.status_code:
            request.session['techchat_cookies'] = c.cookies.output(header='', sep='; ')
            request.session.modified = True
            return redirect('/web/')
        else:
            return render(request, 'login.html', { 'snackbar': str(response.content, 'utf-8') })
    return render(request, 'login.html')

def thread(request, id):
    client = Client()
    response = client.post('/api/users/login/', {'email': 'ajwalhof@mtu.edu', 'password': 'test'})
    response = client.get('/api/boards/', {})
    boards = json.loads(response.content.decode('utf-8'))
    response = client.get('/api/threads/' + id + '/', {})
    thread = json.loads(response.content.decode('utf-8'))
    if request.method == "POST":
        text = request.POST.get('content')
        response = client.post('/api/posts/', {
            'thread': thread.get('id'),
            'content': text
        })
        if response.status_code == 201:
            response = client.get('/api/threads/' + id + '/', {})
            thread = json.loads(response.content.decode('utf-8'))
            return render(request, 'thread.html', {'thread': thread, 'boards': boards, 'snackbar': 'Your comment has been posted!'})
    return render(request, 'thread.html', {'thread': thread, 'boards': boards})

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
