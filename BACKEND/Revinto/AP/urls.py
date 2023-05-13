from django.urls import path
from .views import update_db_AP,AP_monthly



urlpatterns = [
    path("upload",update_db_AP,name="update_db_AP"),
    path("monthly",AP_monthly,name="monthly_AP"),

]
