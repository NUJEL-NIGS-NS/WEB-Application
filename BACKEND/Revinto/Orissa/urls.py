from django.urls import path
from .views import (update_db_OS, OS_monthly, OS_pie, OS_Managers, OS_year_month, OS_unique_pro,
                    OS_BE_mon_sales, OS_BE_mon_sales,
                    OS_geolocation_view, delete_OS_DataBase,
                    OS_distinct_finacial_year,
                    OS_Agency_view,
                    OS_agency_filtered_view,)


urlpatterns = [
    path("upload", update_db_OS, name="update_db_OS"),
    path("monthly", OS_monthly, name="monthly_OS"),
    path("pie", OS_pie, name="pie_OS"),
    path("manager", OS_Managers, name="Managers_OS"),
    path("Bar", OS_year_month, name="Bar_OS"),
    path("pro", OS_unique_pro, name="pro_OS"),
    path("geo", OS_geolocation_view, name="geo_OS"),
    path("be", OS_BE_mon_sales, name="be_OS"),
    path("delete", delete_OS_DataBase, name="delete_db_OS"),
    path("financialyear", OS_distinct_finacial_year, name="financial_OS"),
    path("agency", OS_Agency_view, name="AP_agency"),
    path("agency/filter", OS_agency_filtered_view, name="OS_agency_filter"),










]
