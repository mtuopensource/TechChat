from django.conf.urls import url, include
from . import views

urlpatterns = [
    # ex: /boards/
    url(r'^$', views.index, name='index'),
]
