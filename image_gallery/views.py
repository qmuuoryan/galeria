from django.shortcuts import render

# Create your views here.
def welcome(request):
    return HttpResponse(request, 'home.html')
