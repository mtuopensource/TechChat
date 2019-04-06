from django.conf.urls import url

from web.views.IndexView import index, board, thread, createthread, login, logout

app_name = 'web'

urlpatterns = [
    url(r'^/$', index, name="Home"),
    url(r'board/([0-9]+)/$', board, name='Board'),
    url(r'login/$', login, name='Login'),
    url(r'logout/$', logout, name='Logout'),
    url(r'thread/([0-9]+)/$', thread, name='Thread'),
    url(r'create-thread$', createthread, name='Create Thread'),
]
