from django.shortcuts import render, get_object_or_404
from .models import *

def online(request):
    product_jewelrys = Products.objects.filter(id=10).first()
    all_jewelrys = Products.objects.all()
    categories = Catalogs.objects.all()
    special = Products.objects.filter(id=11).first()
    search_query = request.GET.get('search', '')
    search_catalogs = request.GET.get('catalogs', '')
    sort = request.GET.get('sort', '')

    if search_query and search_catalogs :
        all_jewelrys = Products.objects.filter(name__icontains=search_query, catalogs__name=search_catalogs)
    elif search_catalogs:
        all_jewelrys = Products.objects.filter(catalogs__name=search_catalogs)
    elif search_query:
        all_jewelrys = Products.objects.filter(name__icontains=search_query)
    else: 
        all_jewelrys = Products.objects.all()

    match sort:
        case "A-Z":
            all_jewelrys = all_jewelrys.order_by("name")
        case "Z-A":
            all_jewelrys = all_jewelrys.order_by("-name")
        case "high_price":
            all_jewelrys = all_jewelrys.order_by("-price")
        case "min_price":
            all_jewelrys = all_jewelrys.order_by("price")
        case _:
            all_jewelrys = all_jewelrys.order_by("id")

    context = {
        "product_jewelrys": product_jewelrys,
        "all_jewelrys": all_jewelrys,
        "special": special,
        "search_query": search_query,
        "search_catalogs": search_catalogs,
        "sort": sort,
        "categories": categories,
    }
    return render(request, 'site.html', context)

def cards(request, name_id: int ):
    jeweler = get_object_or_404(Products, id = name_id)
    context = {
        "jeweler": jeweler,
    }
    return render(request, 'card.html', context)
