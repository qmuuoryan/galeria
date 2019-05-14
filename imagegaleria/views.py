from django.http  import HttpResponse
import datetime as dt
from django.shortcuts import render



# Create your views here.
def welcome(request):
    return HttpResponse(request, 'welcome to my gallery')
