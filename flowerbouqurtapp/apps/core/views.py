from django.http import HttpResponse
from django.shortcuts import render

def corepage(request):
    return render(request, 'core/index.html')