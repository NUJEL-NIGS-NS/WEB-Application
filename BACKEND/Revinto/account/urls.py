from django.urls import path
from .views import registration_view,delete_token,user_details
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("register",registration_view,name="register"),
    path("login",obtain_auth_token,name="login"),
    path("logout",delete_token,name='logout'),
    path("detail",user_details,name='details'),


]