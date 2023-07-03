from django.http import HttpRequest, HttpResponse, JsonResponse


def home(request: HttpRequest) -> HttpResponse:

    return HttpResponse('index page')


def about(request: HttpRequest) -> HttpResponse:
    
    return HttpResponse('about page')


def contact(request: HttpRequest) -> HttpResponse:
    
    return HttpResponse('contact page')


def say_hi(request: HttpRequest, first: str, last: str) -> HttpResponse:

    return HttpResponse(f'<h1>Hi, {first} {last}</h1>')


def get_sum(request: HttpRequest) -> JsonResponse:
    # get query params from reqeust
    parmas = request.GET

    a = parmas.get('a', 0)
    b = parmas.get('b', 0)

    return JsonResponse({'sum': int(a) + int(b)})