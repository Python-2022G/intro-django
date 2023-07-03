from django.urls import path

from api.views import home, about, contact, say_hi



urlpatterns = [
    path('home/', home),
    path('about/', about),
    path('contact/', contact),
    path('hi/', say_hi),
    # 'sum/'
]
