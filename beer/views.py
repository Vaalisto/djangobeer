from django.shortcuts import render, get_object_or_404
from .models import Brewery

def index(request):
	all_breweries = Brewery.objects.all()
	return render(request, 'beer/index.html', {'all_breweries': all_breweries})

def detail(request, brewery_id):
	brewery = get_object_or_404(Brewery, id=brewery_id)
	return render(request, 'beer/detail.html', {'brewery': brewery})
