from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.a
class AccountAdminn(UserAdmin):
    list_display=['name','email','username','date_joined','last_login','is_active']
    search_fields = ['email','username']
    readonly_fields = ('date_joined','last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Account,AccountAdminn)