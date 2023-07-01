from django.contrib import admin
from django.urls import path
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    print(request.method)
    print(request.headers['Content-Type'])
    
    return HttpResponse('salom')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
