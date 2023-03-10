from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django import forms

# Register your models here.
@admin.register(Specialite)
class SpecialiteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('libelle', 'description', )

@admin.register(Departement)
class DepartementAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('libelle', 'description', )

@admin.register(Ecole)
class EcoleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('libelle', 'description', )

@admin.register(Formation)
class FormationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('libelle', 'description', )

@admin.register(Specialisations)
class SpecialisationsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('libelle', 'description', )

@admin.register(Clinique)
class CliniqueAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('libelle', 'description', )

@admin.register(Type_Piece)
class EducationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('libelle', 'format', 'code', )

@admin.register(Piece)
class PieceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('date_etablissement', 'date_expiration', 'lieu_etablissemnt', 'numero_piece', 'type_piece', )

@admin.register(Pays)
class PaysAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('code', 'libelle', 'nationnalite', )

@admin.register(Region)
class RegionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pays', 'code','libelle', 'description', )

@admin.register(Ville)
class VilleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('region', 'code','libelle', 'description', )

@admin.register(Profession)
class ProfessionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('code','libelle', 'description', )

