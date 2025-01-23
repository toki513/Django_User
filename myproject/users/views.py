from django.shortcuts import render

def register_now(request):
    return render(request,"users/register.html")
