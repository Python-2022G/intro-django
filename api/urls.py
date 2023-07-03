from django.urls import path

from api.views import home, about, contact



urlpatterns = [
    path('home/', home),
    path('about/', about),
    path('contact/', contact),
]
