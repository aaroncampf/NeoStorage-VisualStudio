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

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })

def locations(request):
    """Renders the locations page."""
    assert isinstance(request, HttpRequest)

    Location1 = Location()
    Location1.Area = 1
    Location1.Bin = 1

    Location2 = Location()
    Location2.Area = 1
    Location2.Bin = 2

    Data = [Location1, Location2]


    return render(request,
        'app/locations.html',
        {
            'title':'Locations',
            'message':'Your application description page.',
            'data':Data
        })
