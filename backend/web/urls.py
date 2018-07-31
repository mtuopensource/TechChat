from django.conf.urls import url
from django.urls import path

from web.views import index, board, thread, createthread, login, logout

app_name = 'web'

urlpatterns = [
    path('', index, name="Home"),
    path('board/<id>/', board, name='Board'),
    path('login/', login, name='Login'),
    path('logout/', logout, name='Logout'),
    path('thread/<id>/', thread, name='Thread'),
    path('create-thread', createthread, name='Create Thread'),
]
