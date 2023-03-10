from django.contrib import admin
from .models import CustomUser,Medcin,Patient
from django.contrib.auth.models import AbstractUser
from import_export.admin import ImportExportModelAdmin
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

# Register your models here.
class UserForm(forms.ModelForm):
    class Meta:
        widgets = {
            'telephone': PhoneNumberPrefixWidget(initial='GN'),
        }

class UserAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    exclude = ('user_permissions', 'groups', )
    ordering = ["created_at"]
    list_display = [ "email", "first_name", "last_name", "created_at", "last_login"]
    form = UserForm

admin.site.register(CustomUser, UserAdmin)

@admin.register(Patient)
class PatientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('user',)

@admin.register(Medcin)
class MedcinAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('user',)

# HTTP_USER_AGENT
# HTTP_SEC_CH_UA
# REMOTE_ADDR
# SERVER_NAME
# SERVER_PORT
# USERDOMAIN
# USERNAME
# OS
# COMPUTERNAME


