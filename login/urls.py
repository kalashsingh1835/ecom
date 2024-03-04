from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('admin/', admin.site.urls ),
    path("",views.sign,name="sign"),
    path("confirmation",views.confirmation,name="confirmation"),
    path("signin",views.signin,name="signin"),
    path("home",views.home,name="home"),
    path("store",views.store,name="store"),
    path("cart",views.cart,name="cart"),
    path("checkout",views.checkout,name="checkout")
    
]