from time import asctime, sleep
import time

from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

# Create your views here.






