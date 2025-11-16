from django.shortcuts import render, get_object_or_404
from .models import *

def online(request):
    product_jewelrys = Products.objects.filter(id=10)
    context = {
        "product_jewelrys": product_jewelrys,
    }
    return render(request, 'site.html', context)

def cards(request):
    return render(request, 'card.html')