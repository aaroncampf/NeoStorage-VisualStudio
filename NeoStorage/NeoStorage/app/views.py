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
