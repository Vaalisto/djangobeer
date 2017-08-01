from django.shortcuts import render, get_object_or_404
from .models import Brewery
from django.views import generic

class IndexView(generic.ListView):
	template_name = 'beer/index.html'
	context_object_name = 'all_breweries'

	def get_queryset(self):
		return Brewery.objects.all()

class DetailView(generic.DetailView):
	model = Brewery
	template_name = 'beer/detail.html'