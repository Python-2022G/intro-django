from django.urls import path

from api.views import home, about



urlpatterns = [
    path('home/', home, name='home-url'),
    path('about/', about, name='about-url'),
]
