from django.urls import path
from . import views

urlpatterns = [
    path('', views.market_landing, name='market_landing'),
]
