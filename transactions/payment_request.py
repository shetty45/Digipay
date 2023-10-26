from django.shortcuts import render,redirect
from bankaccounts.models import Account,Kyc
from django.db.models import Q
from django.contrib import messages
from transactions.models import Transaction

# Create your views here.

def payment_request(request):
    account = Account.objects.all()

    query = request.POST.get("account_number")

    if query:   
        account = account.filter(
            Q(account_number=query)
    ).distinct()

    context = {
        'account': account,
        'query':query
    }
    return render(request,'payment_request/request_payment.html',context)


def amount_request(request,account_number,transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    if request.method == 'POST':
        amount = request.POST.get('amount_request')
        description = request.POST.get('description')

        print(amount)
        print(description)

    context = {
        'account':account,
        'transaction':transaction
    }
    
    return render(request,'payment_request/request_amount.html',context)

def amount_confirmation_request(request, account_number, transaction_id):
    try:
        account = Account.objects.get(account_number=account_number)
        transaction = Transaction.objects.get(transaction_id=transaction_id)
    except:
        messages.warning("Account does not exist")

    pin_number = request.POST.get('pin-number')

    context = {
        'account': account,
        'transaction': transaction,
        'pin-number' : pin_number
    }
    print(pin_number)
    return render(request, "payment_request/request_amount_confirmation.html", context)

def confirmation_success_request(request,account_number,transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    context = {
        'account':account,
        'transaction':transaction
    }
    return render(request,"payment_request/request_confirmation_success.html",context)

def send_confirmation(request,account_number,transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    context = {
        'account':account,
        'transaction':transaction
    }
    return render(request,"payment_request/send_confirmation.html",context)

def send_amount_processing(request,account_number,transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    sender = request.user
    sender_account = request.user.account
    
    if request.method == 'POST':
        pin_number = request.POST.get("pin-number")
        print(pin_number)
        
        if pin_number == request.user.account.pin_number:
            if sender_account.account_balance <= 0 or sender_account.account_balance < transaction.amount:
                messages.warning(request, "Insufficient Funds, find your account and try again.")
            else:
                sender_account.account_balance -= transaction.amount
                sender_account.save()

                account.account_balance += transaction.amount
                account.save()

                transaction.status = "request_settled"
                transaction.save()
            
                messages.success(request,f"settled to { account.user.kyc.full_name } was successfull.")
                return redirect("transaction:send_completed",account.account_number,transaction.transaction_id)
        else:
            messages.warning(request,"Incorrect Pin Number!")
        return redirect("transaction:send_confirmation",account.account_number,transaction.transaction_id)
    else:
        messages.warning(request,"Error Occured")
        return redirect("bankaccounts:dashboard")


def send_amount_completed(request,account_number,transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    context = {
        'account':account,
        'transaction':transaction
    }
    return render(request,"payment_request/send_amount_completed.html",context)