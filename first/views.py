from django.http import HttpResponse

def first(request):
    return HttpResponse("<h1>Hello world! </h1>")

def second_func(request):
    return HttpResponse("Никита")

def my_age(request):
    return HttpResponse("<h1>Мой возраст 26</h1>")