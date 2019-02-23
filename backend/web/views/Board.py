from django.shortcuts import render
from api.models import Board

def board(request, id):
    return render(request, 'board.html', {
        'board': Board.objects.get(id=id)
    })