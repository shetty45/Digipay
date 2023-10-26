from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path("",views.reg,name="reg"),
    path("signin/",views.signin,name="signin"),
    path("logout/",views.user_logout,name="user_logout"),
    
]