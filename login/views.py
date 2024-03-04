from django.shortcuts import render
from django.http import HttpResponse
from .models import User
def sign(request):
    return render(request,"login.html")
def confirmation(request):
    if request.method=='POST':
     names=request.POST.get('name')
     
     passwords=request.POST.get('password')
     emails=request.POST.get('email')
     print(filter(names))
     if filter(names) and filterp(passwords):
         user1=User(name=names,password=passwords,email=emails)
         user1.save()
         return render(request,"confirmation.html")
     if filterp(passwords)==False:
         return HttpResponse("not valid password may contain an special character")

     else:
        return HttpResponse("invalid name")

     
     
def filter(names):
    x=0
    for i in names:
        if 122>ord(i)>65:
            print(ord(i))
            x=x+1
            if x==len(names)-1:
                return True
            continue
          
        else:
            return False
def filterp(passwords):
   x="@!#$"
   y=0
   for i in x :
       if i in passwords:
           y=y+1
           print("y",y)
           continue
   if y==0:
       return False
   else:
       return True
def signin(request):
    return render(request,"signup.html")
def home(request):
    names=request.POST.get("name")
    print(names)
    passwords=request.POST.get("password")
    print(passwords)
    data_exists = User.objects.filter(name=names).values()
    x=0
    for i in data_exists:
        if  i["name"]==names and i["password"]==passwords:
            request="homepage"
            return request
            x=x+1
    return HttpResponse("not the user")
def store(request):
    return render(request,"store.html")
def cart(request):
    return render(request,"cart.html")
def checkout(request):
    return render(request,"checkout.html")
        
        
 
       
       
   


# Create your views here.
