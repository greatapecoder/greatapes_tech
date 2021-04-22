from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return HttpResponse("Greatapes.tech Coming soon")

def index(request):
    return render(request,"greatapes_App/index.html")
