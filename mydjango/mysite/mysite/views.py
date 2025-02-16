from django.shortcuts import  render
from django.http import  HttpResponse

# def index_porjet(request) :
#     return HttpResponse("<h1 style='text-align:center ;'> Bienvenue au  site de lpDawm</h1>")

def index_projet(request):
    return render (request, "base.html")