from django.urls import path
from transactions import transfer
from transactions import payment_request
from transactions import credit_card

app_name = 'transaction'

urlpatterns = [
    path('',transfer.search_user_by_acc_num,name='search'),
    path('amount_transfer/<account_number>/',transfer.amount_transfer,name='amount_transfer'),
    path('amount_transfer_process/<account_number>/', transfer.amount_transfer_process, name='amount_transfer_process'),
    path('transfer_confirmation/<account_number>/<transaction_id>/', transfer.transfer_confirmation, name='transfer_confirmation'),
    path('transfer_process/<account_number>/<transaction_id>/', transfer.transfer_process, name='transfer_process'),
    path('transfer_completed/<account_number>/<transaction_id>/',transfer.transfer_completed,name="transfer_completed"),

    path('payment_request/',payment_request.payment_request, name="payment_request"),
    path('amount_request/<account_number>/<transaction_id>',payment_request.amount_request, name="amount_request"),
    path('amount_confirmation_request/<account_number>/<transaction_id>', payment_request.amount_confirmation_request, name='amount_confirmation_request'),
    path('confirmation_success_request/<account_number>/<transaction_id>', payment_request.confirmation_success_request, name='confirmation_success_request'),

    path('send_confirmation/<account_number>/<transaction_id>',payment_request.send_confirmation, name="send_confirmation"),
    path('send_amount_processing/<account_number>/<transaction_id>', payment_request.send_amount_processing, name='send_amount_processing'),
    path('send_amount_completed/<account_number>/<transaction_id>', payment_request.send_amount_completed, name='send_amount_completed'),

    path('credit_card',credit_card.credit_card,name='credit_card'),
    path('credit_card_bill/<card_id>/',credit_card.credit_card_bill,name="credit_card_bill"),
    path('withdraw_amount/<card_id>/',credit_card.withdraw_amount,name='withdraw_amount'),
    path('credit_card_delete/<card_id>/',credit_card.credit_card_delete,name="credit_card_delete"),

]




