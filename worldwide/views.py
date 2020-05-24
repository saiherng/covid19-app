from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . covid import *

import json
import time
# Create your views here.

c = Covid()

def display(request):

    covid = c.covid_display_total()
    time.sleep(1)
    countries = c.covid_get_countries()

    context = {
        'confirmed' : covid['confirmed'],
        'recovered' : covid['recovered'],
        'deaths' : covid['deaths'],
        'countries' : countries
    }


    return render(request, 'worldwide/worldwide.html', context)

def display_country(request, country):

    #country = "United States of America"
    covid = c.covid_display_country(country)

    context = {
        'country': covid['country'],
        'provinces' : covid['provinces']
    }

    return render(request, 'worldwide/country.html', context)
