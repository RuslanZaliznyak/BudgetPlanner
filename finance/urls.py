from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard_page, name='dashboard_page'),
    path('transactions', views.transactions_page, name='transactions_page')
]
