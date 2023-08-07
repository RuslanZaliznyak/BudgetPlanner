from django.urls import path

from . import views
from .views import DashboardView, TransactionsView, NewTransactionView

app_name = 'finance'


urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('transactions/', TransactionsView.as_view(), name='transactions'),
    path('transactions/new', NewTransactionView.as_view(), name='new-transaction')
]
