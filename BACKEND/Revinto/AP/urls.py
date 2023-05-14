from django.urls import path
from .views import update_db_AP,AP_monthly,AP_pie,AP_Managers



urlpatterns = [
    path("upload",update_db_AP,name="update_db_AP"),
    path("monthly",AP_monthly,name="monthly_AP"),
    path("pie",AP_pie,name="pie_AP"),
    path("manager",AP_Managers,name="Managers_AP"),


]
