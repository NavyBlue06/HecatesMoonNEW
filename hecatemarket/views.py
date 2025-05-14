from django.shortcuts import render

# Create your views here.
def market_landing(request):
    return render(request, 'hecatemarket/market_landing.html')