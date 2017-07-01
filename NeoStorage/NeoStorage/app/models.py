"""
Definition of models.
"""

from django.db import models

#**************************************
# IDs are automatically added for you
#**************************************

# Create your models here.
class Product(models.Model):
	CATG = models.CharField(max_length=200)
	Group = models.CharField(max_length=200)
	Description = models.CharField(max_length=200)
	Vendor = models.ForeignKey('Vendor')
	Location = models.ForeignKey('Location', blank=True, null=True)

class Location(models.Model):
	Area = models.IntegerField()
	Bin = models.IntegerField()

class Vendor(models.Model):
	Name = models.CharField(max_length=200)
	City = models.CharField(max_length=200)
	State = models.CharField(max_length=200)
	Zip = models.CharField(max_length=200)
	Name = models.CharField(max_length=200)
	Name = models.CharField(max_length=200)
	Name = models.CharField(max_length=200)