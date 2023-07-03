from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest) -> HttpResponse:
    print(request.method)
    print(request.headers['Content-Type'])
    
    return HttpResponse('index page')