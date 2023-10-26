from django.shortcuts import render 
from accounts.forms import user_form,user_profile_form,UserRegisterForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="accounts:signin")
def user_logout(request):
    logout(request)
    return redirect("accounts:signin")

def reg(request):
    if request.method == 'POST':
        regi = UserRegisterForm(request.POST)

        if regi.is_valid():
            regi.save()
            username = regi.cleaned_data.get('username')
            messages.success(request,f"hey {username} your account was created successfully")

    else:
        regi = UserRegisterForm()
    return render(request,"account/reg.html",{'regi':regi})

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)
        print(username,password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('bankaccounts:account')
        else:
            return HttpResponse("check your credentials...")
    return render(request,"account/signin.html")



