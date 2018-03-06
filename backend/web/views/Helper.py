import json
from django.test import Client

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

def get_boards_list(client):
    boards_list = str(client.get('/api/boards/').content, 'utf-8')
    return json.loads(boards_list)
