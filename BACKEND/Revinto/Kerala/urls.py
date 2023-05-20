from django.urls import path
from .views import (update_db_KL, KL_monthly, KL_pie, KL_Managers, KL_year_month, KL_unique_pro,
                    KL_BE_mon_sales, KL_BE_mon_sales,
                    KL_geolocation_view, delete_KL_DataBase,
                    KL_distinct_finacial_year,
                    KL_Agency_view,
                    KL_agency_filtered_view,)


urlpatterns = [
    path("upload", update_db_KL, name="update_db_KL"),
    path("monthly", KL_monthly, name="monthly_KL"),
    path("pie", KL_pie, name="pie_KL"),
    path("manager", KL_Managers, name="Managers_KL"),
    path("Bar", KL_year_month, name="Bar_KL"),
    path("pro", KL_unique_pro, name="pro_KL"),
    path("geo", KL_geolocation_view, name="geo_KL"),
    path("be", KL_BE_mon_sales, name="be_KA"),
    path("delete", delete_KL_DataBase, name="delete_db_KL"),
    path("financialyear", KL_distinct_finacial_year, name="financial_KL"),
    path("agency", KL_Agency_view, name="AP_agency"),
    path("agency/filter", KL_agency_filtered_view, name="KL_agency_filter"),



]