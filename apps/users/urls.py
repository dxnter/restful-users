from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create, name='create'),
    url(r'^user/add$', views.add, name='add'),
    url(r'^user/(?P<id>\d+)/edit$', views.edit, name='edit'),
    url(r'^user/(?P<id>\d+)$', views.user, name='show_user'),
    url(r'^user/(?P<id>\d+)/delete$', views.delete, name='delete'),
    url(r'^user/(?P<id>\d+)/update$', views.update, name='update')
]