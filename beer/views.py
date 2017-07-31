from django.http import HttpResponse
from django.shortcuts import render
from .models import Brewery

def index(request):
	all_breweries = Brewery.objects.all()	
	context = {'all_breweries': all_breweries}
	return render(request, 'beer/index.html', context)

def detail(request, brewery_id):
	return HttpResponse("<h2>Details for Brewery id: " + str(brewery_id) + "</h2>")
