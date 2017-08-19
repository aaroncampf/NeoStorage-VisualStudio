"""
Definition of models.
"""

from django.db import models
from django.urls import reverse

#**************************************
# IDs are automatically added for you
#**************************************



# Create your models here.

class Location(models.Model):
	Area = models.IntegerField()
	Bin = models.IntegerField()

	def __str__(self):
		return '%s - %s' % (self.Area, self.Bin)

class Product(models.Model):
	CATG = models.CharField(max_length=200)
	Group = models.CharField(max_length=200)
	Description = models.CharField(max_length=200)
	Vendor = models.ForeignKey('Vendor')
	#Location = models.ForeignKey('Location', blank=True, null=True)

	location = models.OneToOneField(Location, None, primary_key = True, null=False)

	def __str__(self):
		return self.Description



class Vendor(models.Model):
	Name = models.CharField(max_length=200)
	Address = models.CharField(max_length=200, default='')
	City = models.CharField(max_length=200, default='')
	State = models.CharField(max_length=200, default='')
	Zip = models.CharField(max_length=200, default='')
	Phone = models.CharField(max_length=200, default='')
	Email = models.CharField(max_length=200, default='')

	def __str__(self):
		return self.Name

	def get_absolute_url(self):
		return reverse('vendor', kwargs={'pk': self.pk})