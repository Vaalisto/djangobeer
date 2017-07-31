from django.conf.urls import url
from . import views

app_name = 'beer'

urlpatterns = [
	# /beer/
	url(r'^$', views.index, name='index'),

	# /beer/712/
	url(r'^(?P<brewery_id>[0-9]+)/$', views.detail, name='detail'),
]