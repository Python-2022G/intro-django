from django.http import HttpRequest
from django.shortcuts import render

def home(request: HttpRequest, name):

    return render(request, 'home.html', {'name': name})
