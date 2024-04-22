from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home.html',views.home,name="home"),
    path('login.html',views.login,name="login"),
    path('aqi.html',views.aqi,name="aqi"),
    path('nutri.html',views.nutri,name="nutri")
]

    
