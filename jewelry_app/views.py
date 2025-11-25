from django.shortcuts import render, get_object_or_404
from .models import *

def online(request):
    product_jewelrys = Products.objects.filter(id=10).first()
    all_jewelrys = Products.objects.all()
    special = Products.objects.filter(id=8).first()
    search_query = request.POST.get('search', '')
    search_catalogs = request.POST.get('catalogs', )
    sort = request.POST.get('sort', '')

    if search_query and search_catalogs :
        all_jewelrys = Products.objects.filter(name__icontains=search_query, search_catalogs__name=search_catalogs)
    elif search_catalogs:
        all_jewelrys = Products.objects.filter(search_catalogs__name=search_catalogs)
    elif search_query:
        all_jewelrys = Products.objects.filter(name__icontains=search_query)

    match sort:
        case "date-reverse":
            all_jewelrys

    context = {
        "product_jewelrys": product_jewelrys,
        "all_jewelrys": all_jewelrys,
        "special": special,
        "search_query": search_query,
        "search_catalogs": search_catalogs,
        "sort": sort,
    }
    return render(request, 'site.html', context)

def cards(request, name_id: int ):
    jeweler = get_object_or_404(Products, id = name_id)
    context = {
        "jeweler": jeweler,
    }
    return render(request, 'card.html', context)
