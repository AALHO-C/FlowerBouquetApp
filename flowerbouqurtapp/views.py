from django.http import HttpResponse
from django.shortcuts import render
from . import *

def home(request):
    return render(request, 'index.html')