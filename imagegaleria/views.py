from django.http  import HttpResponse,Http404
from django.http  import HttpResponse
import datetime as dt
from django.shortcuts import render,redirect

from django.shortcuts import render



# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
