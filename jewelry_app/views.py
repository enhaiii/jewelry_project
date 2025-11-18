from django.shortcuts import render, get_object_or_404
from .models import *

def online(request):
    product_jewelrys = Products.objects.filter(id=10).first()
    all_jewelrys = Products.objects.all()
    special = Products.objects.filter(id=8).first()
    context = {
        "product_jewelrys": product_jewelrys,
        "all_jewelrys": all_jewelrys,
        "special": special,
    }
    return render(request, 'site.html', context)

def cards(request, name_id: int ):
    jeweler = get_object_or_404(Products, id = name_id)
    context = {
        "jeweler": jeweler,
    }
    return render(request, 'card.html', context)