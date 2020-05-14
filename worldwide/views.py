from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . covid import *



# Create your views here.
def display(request):

    covid = covid_display_total().json()[0]

    context = {
        'confirmed' : covid['confirmed'],
        'recovered' : covid['recovered'],
        'deaths' : covid['deaths']
    }
    return render(request, 'worldwide/index.html', context)
