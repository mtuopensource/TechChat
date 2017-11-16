from django.shortcuts import render
from django.http import HttpResponse

from .models import Board

def index(request):
    board_list = Board.objects.order_by('-title')[:5]
    output = ', '.join([b.title for b in board_list])
    return HttpResponse(output)
