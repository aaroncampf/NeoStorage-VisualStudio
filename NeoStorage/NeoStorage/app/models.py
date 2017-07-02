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
	Address = models.CharField(max_length=200, default='')
	City = models.CharField(max_length=200, default='')
	State = models.CharField(max_length=200, default='')
	Zip = models.CharField(max_length=200, default='')
	Phone = models.CharField(max_length=200, default='')
	Email = models.CharField(max_length=200, default='')