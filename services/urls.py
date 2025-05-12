from django.urls import path
from . import views

urlpatterns = [
    path('birth-chart/', views.birth_chart_request, name='birth_chart'),

    # Future routes for your other services:
    path('ask-a-witch/', views.ask_a_witch, name='ask_a_witch'),
    path('ritual-request/', views.ritual_request, name='ritual_request'),
    path('dream-interpretation/', views.dream_interpretation, name='dream_interpretation'),
    path('contact-medium/', views.medium_contact, name='medium_contact'),
]
