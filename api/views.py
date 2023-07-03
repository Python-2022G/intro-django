from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:

    return HttpResponse('index page')


def about(request: HttpRequest) -> HttpResponse:
    
    return HttpResponse('about page')


def contact(request: HttpRequest) -> HttpResponse:
    
    return HttpResponse('contact page')


def say_hi(request: HttpRequest) -> HttpResponse:
    # get query params from reqeust
    parmas = request.GET
    name = parmas.get('name')

    return HttpResponse(f'<h1>Hi, {name}</h1>')


def get_sum(request: HttpRequest) -> HttpResponse:
    # your code: a, b

    return HttpResponse(f'sum: {}')