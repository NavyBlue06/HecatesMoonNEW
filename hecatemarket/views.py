from django.shortcuts import render
from boxes.models import Product  # correct name of model Navahlicious!

def market_landing(request):
    return render(request, 'hecatemarket/market_landing.html')

def market_items(request):
    items = Product.objects.filter(is_available=True)
    return render(request, 'hecatemarket/market_items.html', {'items': items})
