"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from app.models import *


def home(request):
	"""Renders the home page."""
	assert isinstance(request, HttpRequest)
	return render(request,
		'app/index.html',
		{
			'title':'Home Page',
			'year':datetime.now().year,
		})

def locations(request):
	"""Renders the locations page."""
	assert isinstance(request, HttpRequest)

	if Location.objects.all().count() == 0:
		Location1 = Location()
		Location1.Area = 1
		Location1.Bin = 1
		Location1.save()

		Location2 = Location()
		Location2.Area = 1
		Location2.Bin = 2
		Location2.save()

	return render(request,
		'app/locations.html',
		{
			'title':'Locations',
			'message':'Your application description page.',
			'data':Location.objects.all()
		})


def vendor(request, id):
	"""Renders the vendors page."""
	assert isinstance(request, HttpRequest)

	return render(request,
		'app/vendor.html',
		{
			'title':'vendor',
			'message':'Your application description page.',
			'data':Vendor.objects.all()[int(id)]
		})

def vendors(request):
	"""Renders the vendors page."""
	assert isinstance(request, HttpRequest)
	
	if Vendor.objects.all().count() == 0:
		Vendor1 = Vendor.objects.create(Name = "Test Vendor", Address = "1111", City = "Portland", Zip ="87654", 
										Phone="(555) 555-5555", Email ="Test@example.com")
		Vendor1.save() 

		Vendor2 = Vendor.objects.create(Name = "Test Vendor2", Address = "2222", City = "Salen", Zip ="56980", 
										Phone="(666) 666-6666", Email ="Example@example.com")
		Vendor2.save()  

	return render(request,
		'app/vendors.html',
		{
			'title':'vendors',
			'message':'Your application description page.',
			'data':Vendor.objects.all()
		})


def products(request):
	"""Renders the products page."""
	assert isinstance(request, HttpRequest)

	if Product.objects.all().count() == 0:
		Vendor1 = Vendor.objects.all()[0]
		Vendor2 = Vendor.objects.all()[1]
		Location1 = Location.objects.all()[0]
		Location2 = Location.objects.all()[1]

		Product1 = Product.objects.create(CATG = "A", Group = "A-1", Description = "Towels", Vendor = Vendor1, Location = Location1)
		Product1.save()
		Product2 = Product.objects.create(CATG = "A", Group = "A-2", Description = "Toilet Paper", Vendor = Vendor2, Location = Location2)
		Product2.save()

	return render(request,
		'app/products.html',
		{
			'title':'products',
			'message':'Your application description page.',
			'data':Product.objects.all()
		})
