from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My Workshop</h1>")

def detail(request):
    return HttpResponse("<h1>We are going to learn Django</h1>")
