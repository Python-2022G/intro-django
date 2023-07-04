from django.http import HttpRequest
from django.shortcuts import render

def home(request: HttpRequest):

    users = [
        {
            "first": "Ali",
            "last": "Valiyev"
        },
        {
            "first": "Ali1",
            "last": "Valiyev1"
        },
        {
            "first": "Ali2",
            "last": "Valiyev2"
        }
    ]

    return render(request, 'home.html', {'users': users})
