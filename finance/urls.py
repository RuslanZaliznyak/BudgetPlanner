from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('add-transaction', views.add_transaction, name='add-transaction'),
    path('add-budget', views.add_budget, name='add-budget'),
    path('add-wallets', views.add_wallets, name='add-wallets'),
    path('add-loan', views.add_loan, name='add-loan'),
    path('add-mandatory-pay', views.add_mandatory_pay, name='add-mandatory-pay')
]
