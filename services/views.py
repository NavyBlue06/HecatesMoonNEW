from django.shortcuts import render
from .forms import BirthChartRequestForm
# Create your views here.

def birth_chart_request(request):
    if request.method == 'POST':
        form = BirthChartRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'services/success.html')
    else:
        form = BirthChartRequestForm()

    return render(request, 'services/birth_chart_request.html', {'form': form})
