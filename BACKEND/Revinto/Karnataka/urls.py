from django.urls import path
from .views import (update_db_KA, KA_monthly, KA_pie, KA_Managers, KA_year_month, KA_unique_pro,
                    KA_BE_mon_sales, KA_BE_mon_sales,
                    KA_geolocation_view, delete_KA_DataBase,
                    KA_distinct_finacial_year,
                    KA_Agency_view,
                    KA_agency_filtered_view,)


urlpatterns = [
    path("upload", update_db_KA, name="update_db_KA"),
    path("monthly", KA_monthly, name="monthly_KA"),
    path("pie", KA_pie, name="pie_KA"),
    path("manager", KA_Managers, name="Managers_KA"),
    path("Bar", KA_year_month, name="Bar_KA"),
    path("pro", KA_unique_pro, name="pro_KA"),
    path("geo", KA_geolocation_view, name="geo_KA"),
    path("be", KA_BE_mon_sales, name="be_KA"),
    path("delete", delete_KA_DataBase, name="delete_db_KA"),
    path("financialyear", KA_distinct_finacial_year, name="financial_KA"),
    path("agency", KA_Agency_view, name="AP_agency"),
    path("agency/filter", KA_agency_filtered_view, name="KA_agency_filter"),



]
