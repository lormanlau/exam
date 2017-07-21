from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^quotes$', views.dashboard),
	url(r'^users/(?P<id>\d+)$', views.userinfo),
	# url(r'^users/logout$', views.index),
	# url(r'^users/login$', views.login),
	url(r'^users/register$', views.register),

]