from django.urls import path
from .views import (update_db_AP, AP_monthly, AP_pie, AP_Managers, AP_year_month, AP_unique_pro,
                    Ap_BE_mon_sales, Ap_BE_mon_sales,
                    AP_geolocation_view, delete_AP_DataBase,
                    AP_distinct_finacial_year,
                    AP_Agency_view,
                    AP_agency_filtered_view,)


urlpatterns = [
    path("upload", update_db_AP, name="update_db_AP"),
    path("monthly", AP_monthly, name="monthly_AP"),
    path("pie", AP_pie, name="pie_AP"),
    path("manager", AP_Managers, name="Managers_AP"),
    path("Bar", AP_year_month, name="Bar_AP"),
    path("pro", AP_unique_pro, name="pro_AP"),
    path("geo", AP_geolocation_view, name="geo_AP"),
    path("be", Ap_BE_mon_sales, name="be_AP"),
    path("delete", delete_AP_DataBase, name="delete_db_Ap"),
    path("financialyear", AP_distinct_finacial_year, name="financial_AP"),
    path("agency", AP_Agency_view, name="AP_agency"),
    path("agency/filter", AP_agency_filtered_view, name="AP_agency_filter"),










]
