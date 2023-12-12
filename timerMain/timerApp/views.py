from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'timerApp/index.html')

def trial(request):
    return render(request, 'timerApp/trial.html')

def register(request):
    return render(request, 'timerApp/register.html')

def login(request):
    return render(request, 'timerApp/login.html')


