from django.urls import path

from api.views import home, about, contact, say_hi, get_sum



urlpatterns = [
    path('home/', home),
    path('about/', about),
    path('contact/', contact),
    path('hi/<first>/<last>', say_hi),
    path('sum/', get_sum),
]
