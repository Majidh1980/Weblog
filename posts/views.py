from django.http import HttpResponse


def index(request):

    return HttpResponse('<h1>Welcome to django.</h1>')


def home(request):
    return HttpResponse('<h3>Welcome to my blog... .</h3>')
