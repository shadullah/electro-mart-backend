from django.http import HttpResponse

def home(req):
    return HttpResponse("Electro backend is running")