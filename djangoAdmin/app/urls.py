from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^veiculo/listar/(?P<categoria>[\w\-]+)/$', veiculo_list, name='veiculo_list'),
    url(r'^veiculo/profile/(?P<pk>[0-9]+)/$', veiculo_profile, name='veiculo_profile'),
]