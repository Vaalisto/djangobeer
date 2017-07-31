from django.http import Http404
from django.shortcuts import render
from .models import Brewery

def index(request):
	all_breweries = Brewery.objects.all()
	return render(request, 'beer/index.html', {'all_breweries': all_breweries})

def detail(request, brewery_id):
	try:
		brewery = Brewery.objects.get(id=brewery_id)
	except Brewery.DoesNotExist:
		raise Http404("Brewery does not exist")
	return render(request, 'beer/detail.html', {'brewery': brewery})
