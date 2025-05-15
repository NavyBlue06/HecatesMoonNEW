from django.shortcuts import render
from boxes.models import Product

# Create your views here.
def market_landing(request):
    return render(request, 'hecatemarket/market_landing.html')

def market_items(request):
    items = Product.objects.filter(is_available=True).exclude(category__icontains='box')
    return render(request, 'hecatemarket/market_items.html', {'items': items})