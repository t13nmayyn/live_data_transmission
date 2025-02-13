from django.contrib import admin
from django.urls import path
from. import views 
urlpatterns = [
    path("",views.home,name='home'),
    path("generate-num/",views.create_random_array,name='generate-num'),
    path("login/",views.loginUser,name='login')
    
]
