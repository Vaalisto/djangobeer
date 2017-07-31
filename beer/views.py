from django.http import HttpResponse
from django.template import loader
from .models import Brewery

def index(request):
	all_breweries = Brewery.objects.all()
	template = loader.get_template('beer/index.html')
	context = {
		'all_breweries': all_breweries,
	}
	return HttpResponse(template.render(context, request))

def detail(request, brewery_id):
	return HttpResponse("<h2>Details for Brewery id: " + str(brewery_id) + "</h2>")
