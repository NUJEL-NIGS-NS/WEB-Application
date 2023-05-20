from django.urls import path
from .views import state_list_view

urlpatterns = [
    path("state",state_list_view,name="all_states")
]
