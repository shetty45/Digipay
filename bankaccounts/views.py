from django.shortcuts import render
from bankaccounts.forms import kyc_form
from django.shortcuts import redirect   
from django.contrib import messages
from bankaccounts.models import Account
from bankaccounts.models import Kyc
from transactions.models import Transaction
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.

@login_required(login_url="accounts:signin")
def account(request):
    account = Account.objects.get(user=request.user)
    kyc = Kyc.objects.all()

    context = {
        'kyc' : kyc,
        'account' : account 
    }
    return render(request,'account/account.html',context)
    
def kyc_reg(request):
    user = request.user
    account = Account.objects.get(user=user)

    try:
        kyc = Kyc.objects.get(user=user)
    except:
        kyc = None

    if request.method == "POST":
        form = kyc_form(request.POST,request.FILES,instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save() 
            messages.success(request,"KYC form submitted successfully,In review now.")
            return redirect("dashboard")
    else:
        form = kyc_form(instance=kyc)
    context = {
        "account" : account,
        "form" : form,
        "kyc" : kyc
    }
    return render(request,'account/kyc_form.html',context)

def dashboard(request):
    user = request.user
    account = Account.objects.get(user=user)
    transaction = Transaction.objects.all()
    kyc = Kyc.objects.get(user=user)
    context = {
        'account':account,
        'transaction': transaction,
        'kyc':kyc,
    }
    return render(request,'account/dashboard.html',context)


def transaction_lists(request):
    user = request.user
    account = Account.objects.get(user=user)
    
    transaction = Transaction.objects.all()
    kyc = Kyc.objects.get(user=user)
    query1 = request.POST.get("request_sent")
    query2 = request.POST.get("completed")
    if query1:
        transaction=transaction.filter(
            Q(status=query1)
        ).distinct()
    if query2:
        transaction=transaction.filter(
            Q(status=query2)
        ).distinct()
    context = {
        'account':account,
        'transaction': transaction,
        'kyc':kyc,
        'query1':query1,
        'query2':query2,
    }

    return render(request, "transactions/transaction_list.html",context)

def transaction_details(request,transaction_id):
    user=request.user
    account = Account.objects.get(user=user)
   
    kyc = Kyc.objects.get(user=request.user)
    kyc = Kyc.objects.get(user=user)
    
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    reciever = account.user
    
    
    context = {
        'account':account,
        'kyc':kyc,
        'transaction':transaction,
        'reciever':reciever,
        
    }
    return render(request,'transactions/transaction_details.html',context)