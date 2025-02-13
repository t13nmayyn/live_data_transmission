from django.shortcuts import render,redirect
import random,time
from .models import Display
from django.http import JsonResponse
from django.utils.timezone import now
# Create your views here.
#
def home(request):
    display=Display.objects.all().order_by("updated")
    context={"display":display}

    return render(request,"home.html",context=context)



def generate_random_array_at_time(request):
    array = [[random.randint(0, 9) for _ in range(4)] for _ in range(3)]
    display_entry = Display.objects.create(array=array)

    return render(request,"new.html")
    # return JsonResponse({
    #     "array": array,
    #     "updated": display_entry.updated.strftime("%Y-%m-%d %H:%M:%S")  # Format the timestamp for better readability
    # })


from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
def loginUser(request):
    # if request.user.is_authenticated():
    #     return redirect("home")
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is None:
            login(request,user)
            return redirect('home')
    return render(request,"login.html")


# from django.conf.auth?




def create_random_array(request):
    count=0
    while True:

        # delay=random.uniform()
    
        array=[[random.randint(0,9) for _ in range(4)] for _ in range(3)]
        display=Display.objects.create(array=array,updated=now())
        time.sleep(random.randint(1,4))
        count=count+1
        
        if count==5:
            break
    new_display=Display.objects.last()
    context={"display":new_display}
    return render(request,"new.html",context)



    

