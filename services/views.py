from django.shortcuts import render
from .forms import (
    BirthChartRequestForm,
    WitchQuestionForm,
    RitualRequestForm,  
    DreamSubmissionForm,
    MediumContactForm
    )
# Create your views here.

def birth_chart_request(request):
    if request.method == 'POST':
        form = BirthChartRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'services/thank_you.html')
    else:
        form = BirthChartRequestForm()

    return render(request, 'services/birth_chart_request.html', {'form': form})

def ask_a_witch(request):
    if request.method == 'POST':
        form = WitchQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'services/thank_you.html')
    else:
        form = WitchQuestionForm()

    return render(request, 'services/ask_a_witch.html', {'form': form})

def ritual_request(request):
    if request.method == 'POST':
        form = RitualRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'services/thank_you.html')
    else:
        form = RitualRequestForm()
    return render(request, 'services/ritual_request.html', {'form': form})


def dream_interpretation(request):
    if request.method == 'POST':
        form = DreamSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'services/thank_you.html')
    else:
        form = DreamSubmissionForm()
    return render(request, 'services/dream_interpretation.html', {'form': form})


def medium_contact(request):
    if request.method == 'POST':
        form = MediumContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'services/thank_you.html')
    else:
        form = MediumContactForm()
    return render(request, 'services/contact_medium.html', {'form': form})