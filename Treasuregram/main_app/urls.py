from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add_treasure, name='add_treasure'),
    url(r'^add/post_url/$', views.post_treasure, name='post_treasure'),
]
