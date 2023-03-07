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

class EduAdmin(admin.StackedInline):
    model= Education

class ExpAdmin(admin.StackedInline):
    model= Experience

# TabularInline
# StackedInline

class DispAdmin(admin.StackedInline):
    model= Disponibilite

# @admin.register(Medcin)
class MedcinAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('IDMedcin', 'nom', 'prenom', 'email', 'photo', 'telephone', 'pays', 'adresse', 'bio', 'anniversaire', 'genre', 'tags', 'specialite', 'views', 'is_popular', 'twitter', 'facebook', 'instagram', 'linkdin', )
    ordering=('updated',)  
    inlines=[EduAdmin,ExpAdmin,DispAdmin]
    list_filter = ('status', 'genre','specialite','departement')

admin.site.register(Medcin,MedcinAdmin)

@admin.register(Education)
class EducationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('formation', 'description', 'date_debut', 'date_fin', )

@admin.register(Experience)
class ExperienceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('poste', 'description', 'date_debut', 'date_fin', )

@admin.register(Certificat)
class CertificatAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('titre', 'date', 'medcin', )

@admin.register(Galerie)
class GalerieAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('titre', 'description', 'medcin')

@admin.register(Disponibilite)
class DisponibiliteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('joursDisponibilite', 'medcin', 'description', 'heure_debut_lundi', 'heure_fin_lundi', 'heure_debut_mardi', 'heure_fin_mardi', 'heure_debut_mercredi', 'heure_fin_mercredi', 'heure_debut_jeudi', 'heure_fin_jeudi', 'heure_debut_vendredi', 'heure_fin_vendredi', 'heure_debut_samedi', 'heure_fin_samedi', 'heure_debut_dimanche', )

@admin.register(SpecialisationMedcin)
class SpecialisationMedcinAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('libelle', 'medcin', 'description',)