from django.shortcuts import render

def online(request):
    return render(request, 'site.html')

def cards(request):
    return render(request, 'card.html')