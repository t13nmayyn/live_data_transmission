from django.shortcuts import render,redirect
import random,time
from .models import Display
from django.http import JsonResponse
# Create your views here.
#
def home(request):
    return render(request,"home.html")



def generate_random_array_at_time(request):
    array = [[random.randint(0, 9) for _ in range(4)] for _ in range(3)]
    display_entry = Display.objects.create(array=array)
    return JsonResponse({
        "array": array,
        "updated": display_entry.updated.strftime("%Y-%m-%d %H:%M:%S")  # Format the timestamp for better readability
    })



def display_array(request):
    # Get the most recent Display entry (latest created entry)
    display = Display.objects.last()
    return render(request, "main.html", {'display': display})




