from django.contrib import admin
from django.urls import path
from. import views 
urlpatterns = [
    path("",views.home,name='home'),
    path("generate-num",views.generate_random_array_at_time,name='generate-num')
]
