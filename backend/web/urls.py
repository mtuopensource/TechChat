from django.conf.urls import url
from django.urls import path

from web.views import index, board, thread, createthread, login

app_name = 'web'

urlpatterns = [
    path('', index, name="TechChat Home"),
    path('board/<id>/', board, name='Board'),
    path('login/', login, name='TechChat Login'),
    path('thread/<id>/', thread, name='Thread'),
    path('create-thread', createthread, name='Create Thread'),
]
