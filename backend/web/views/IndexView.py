import requests
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.test import Client
from api.views.BoardViewSet import BoardViewSet
from django.template.loader import render_to_string

from .Helper import *

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        return authenticate(request, username, password)
    return render(request, 'login.html')

@check_authentication
def logout(request, client=None):
    request.session.flush()
    return redirect('/web/login/')

@check_authentication
def index(request, client=None):
    boards_list = get_boards_list(client)
    return render(request, 'index.html', {
        'boards_list': boards_list
    })

@check_authentication
def board(request, id, client=None):
    board = get_board(client, id)
    boards_list = get_boards_list(client)
    return render(request, 'board.html', {
        'board': board,
        'boards_list': boards_list
    })

@check_authentication
def thread(request, id, client=None):
    boards_list = get_boards_list(client)
    snackbar = None
    if request.method == 'POST':
        comment_text = request.POST['content']
        if post_comment(client, id, comment_text):
            snackbar = 'Your comment has been posted!'
    thread = get_thread(client, id)
    return render(request, 'thread.html', {
        'thread': thread,
        'boards_list': boards_list,
        'snackbar': snackbar
    })
    
@check_authentication
def createthread(request, client=None):
    boards_list = get_boards_list(client)
    if request.method == "POST":
        board = request.POST['board']
        thread_title = request.POST['title']
        thread_content = request.POST['content']
        id = create_thread(client, board, thread_title, thread_content)
        if id is not None:
            return redirect('/web/thread/' + id + '/')
    return render(request, 'thread-create.html', {
        'boards_list': boards_list
    })
