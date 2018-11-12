from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^faculty/', views.faculty, name='faculty'),
	url(r'^specialization/(?P<pk>[0-9]+)/$', views.specialization, name='specialization'),
	url(r'^discipline/(?P<pk>[0-9]+)/$', views.discipline, name='discipline'),
	url(r'^cabinet/$', views.cabinet, name='cabinet'),
	url(r'^vote/(?P<pk>[0-9]+)/(?P<specialization>[0-9]+)/(?P<faculty>[0-9]+)/(?P<teacher>[0-9]+)/(?P<student>[0-9]+)/$', views.vote, name='vote'),
	url(r'^remove/(?P<pk>[0-9]+)/$', views.remove, name='remove'),
	
]