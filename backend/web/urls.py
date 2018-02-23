from django.conf.urls import url

from web.views import index, board

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^board/(?P<id>\w+)/$', board, name='board'),
]
