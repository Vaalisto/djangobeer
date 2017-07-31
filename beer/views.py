from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>Beer homepage</h1>")

def detail(request, beer_id):
	return HttpResponse("<h2>Details for Beer id: " + str(beer_id) + "</h2>")
