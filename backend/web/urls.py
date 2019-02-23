from django.conf.urls import url, include
from web.views import board

urlpatterns = [
    url(r'^board/(?P<id>\d+)/$', board, name="Board"),
]
