from django.conf.urls import url

from web.views import index, board, thread, createthread

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^board/(?P<id>\w+)/$', board, name='board'),
    url(r'^thread/(?P<id>\w+)/$', thread, name='thread'),
    url(r'^new/$', createthread, name='createthread'),
]
