from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, world! Your Django app is running.</h1>")