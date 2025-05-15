from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import (
    BirthChartRequestForm,
    WitchQuestionForm,
    RitualRequestForm,
    DreamSubmissionForm,
    MediumContactForm
)

def services_home(request):
    if request.method == 'POST':
        if 'birth_chart_submit' in request.POST:
            form = BirthChartRequestForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Birth chart request submitted!")
                return redirect('services_home')
        elif 'witch_question_submit' in request.POST:
            form = WitchQuestionForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Witch question submitted!")
                return redirect('services_home')
        elif 'ritual_request_submit' in request.POST:
            form = RitualRequestForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Ritual request submitted!")
                return redirect('services_home')
        elif 'dream_submit' in request.POST:
            form = DreamSubmissionForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Dream interpretation submitted!")
                return redirect('services_home')
        elif 'medium_contact_submit' in request.POST:
            form = MediumContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Medium message submitted!")
                return redirect('services_home')

    context = {
        'birth_form': BirthChartRequestForm(),
        'witch_form': WitchQuestionForm(),
        'ritual_form': RitualRequestForm(),
        'dream_form': DreamSubmissionForm(),
        'medium_form': MediumContactForm(),
        'birth_chart_price': 60,
        'ask_a_witch_price': 45,
        'ritual_request_price': 60,
        'dream_interpretation_price': 50,
        'medium_contact_price': 100,
    }
    return render(request, 'services/services.html', context)
