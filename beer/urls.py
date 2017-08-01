from django.conf.urls import url
from . import views

app_name = 'beer'

urlpatterns = [
	# /beer/
	url(r'^$', views.IndexView.as_view(), name='index'),

	# /beer/712/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]