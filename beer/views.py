from django.http import HttpResponse
from .models import Brewery

def index(request):
	all_breweries = Brewery.objects.all()
	html = ''
	for brewery in all_breweries:
		url = '/beer/' + str(brewery.id) + '/'
		html += '<a href="' + url + '">' + brewery.name + '</a><br>'
	return HttpResponse(html)

def detail(request, brewery_id):
	return HttpResponse("<h2>Details for Brewery id: " + str(brewery_id) + "</h2>")
