from django.db import models

class Brewery(models.Model):
	name = models.CharField(max_length=250)
	year = models.PositiveIntegerField()

	def __str__(self):
		return self.name + ', ' + str(self.year)

class Beer(models.Model):
	name = models.CharField(max_length=250)
	brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)

	def __str__(self):
		return self.name