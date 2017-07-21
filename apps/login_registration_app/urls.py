from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^quotes$', views.dashboard),
	url(r'^users/(?P<id>\d+)$', views.userinfo),
	url(r'^users/logout$', views.logout),
	url(r'^users/login$', views.login),
	url(r'^users/register$', views.register),
	url(r'^quotes/add$', views.addquote),
	url(r'^quotes/addfavorites/(?P<id>\d+)$', views.addfavorites),
]