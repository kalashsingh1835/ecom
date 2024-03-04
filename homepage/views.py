from django.shortcuts import render

# Create your views here.
def homepage(request):
   return render(request,"main.html")
def store(request):
    return render(request,"store.html")
