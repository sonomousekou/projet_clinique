from django.contrib import admin
from .models import (
    Patient, RendezVous
)
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# @admin.register(Patient)
# class PatientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ('IDPatient', 'photo', 'signature', 'ville', 'piece', 'profession', )

@admin.register(RendezVous)
class RendezVousAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('patient', 'medcin', 'date', 'heure_debut', 'heure_fin', 'etat', 'prix', )
