from django.urls import path
from bankaccounts import views

app_name = 'bankaccounts'

urlpatterns = [
    path("",views.kyc_reg,name="kyc"),
    path('account/',views.account,name='account'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('transaction_lists/',views.transaction_lists,name='transaction_lists'),
    path('transaction_details/<transaction_id>/',views.transaction_details,name="transaction_details"),

] 

