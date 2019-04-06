import json
from django.test import Client
from django.shortcuts import render, redirect

def get_client(request):
    if 'techchat_cookies' in request.session:
        cookie = request.session['techchat_cookies'] # TODO Constants
        return Client(HTTP_COOKIE=cookie)
    return None

def check_authentication(func):
    def wrapper(*args, **kwargs):
        client = get_client(next(x for x in args))
        if client is not None:
            return func(*args, **dict(kwargs, client=client))
        return redirect('/web/login/')
    return wrapper

def get_board(client, id):
    board = str(client.get(f'/api/boards/{id}/').content, 'utf-8')
    return json.loads(board)

def get_thread(client, id):
    thread = str(client.get(f'/api/threads/{id}/').content, 'utf-8')
    return json.loads(thread)

def get_boards_list(client):
    boards_list = str(client.get('/api/boards/').content, 'utf-8')
    return json.loads(boards_list)

def post_comment(client, id, comment_text):
    response = client.post('/api/posts/', {
        'thread':  id,
        'content': comment_text
    })
    return response.status_code == 201

def create_thread(client, board, thread_title, thread_content):
    response = client.post('/api/threads/', {
        'board': board,
        'title': thread_title,
        'content': thread_content
    })
    if response.status_code == 201:
        return json.loads(response.content.decode('utf-8')).get('id')
    return None

def authenticate(request, username, password):
    client = Client()
    response = client.post('/api/token/', {
        'username':    username,
        'password': password
    })
    if response.status_code == 200:
        request.session['techchat_cookies'] = client.cookies.output(header='', sep=';') # TODO Constants
        request.session.modified = True
        return redirect('/web/')
    message = json.loads(str(response.content, 'utf-8'))
    return render(request, 'login.html', {
        'snackbar': message['detail']
    })
