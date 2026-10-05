from django.shortcuts import render
from .models import products
# Create your views here.

def Product(request):
    return render(request , 'products/product.html' , {'Data':products})


def Products(request):
    return render(request , 'products/products.html' , {'Data':products.objects.all()})