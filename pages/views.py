from django.shortcuts import render
from .models import Login 


# Create your views here.

def ShowIndex(request):
    return render(request,'pages/index.html',{'name':'','age':'25'})


def about(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            Data = Login(username=username, password=password)
            Data.save()

    return render(request,'pages/about.html')



    