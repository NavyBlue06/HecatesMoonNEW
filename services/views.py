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
    }
    return render(request, 'services/services.html', context)
