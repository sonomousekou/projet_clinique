from django.urls import path
from core import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('rendezVouss/', views.rendezVous_list),
    path('rendezVouss/<int:pk>/', views.rendezVous_detail),

    path('specialites/', views.specialite_list),
    path('specialites/<str:pk>/', views.specialite_detail),

    path('departements/', views.departement_list),
    path('departements/<str:pk>/', views.departement_detail),
    
    path('ecoles/', views.ecole_list),
    path('ecoles/<str:pk>/', views.ecole_detail),

    path('formations/', views.formation_list),
    path('formations/<str:pk>/', views.formation_detail),

    path('specialisations/', views.specialisations_list),
    path('specialisations/<str:pk>/', views.specialisations_detail),

    path('cliniques/', views.clinique_list),
    path('cliniques/<str:pk>/', views.clinique_detail),

    path('medcins/', views.medcin_list),
    path('medcins/<str:pk>/', views.medcin_detail),

    path('educations/', views.education_list),
    path('educations/<str:pk>/', views.education_detail),

    path('experiences/', views.experience_list),
    path('experiences/<str:pk>/', views.experience_detail),


    path('certificats/', views.certificat_list),
    path('certificats/<str:pk>/', views.certificat_detail),

    path('galeries/', views.galerie_list),
    path('galeries/<str:pk>/', views.galerie_detail),

    path('disponibilites/', views.disponibilite_list),
    path('disponibilites/<str:pk>/', views.disponibilite_detail),

    path('specialisationMedcins/', views.specialisationMedcin_list),
    path('specialisationMedcins/<str:pk>/', views.specialisationMedcin_detail),

    path('pays/', views.pays_list),
    path('pays/<str:pk>/', views.pays_detail),

    path('regions/', views.region_list),
    path('regions/<str:pk>/', views.region_detail),

    path('villes/', views.ville_list),
    path('villes/<str:pk>/', views.ville_detail),

    path('professions/', views.profession_list),
    path('professions/<str:pk>/', views.profession_detail),

    path('patients/', views.patient_list),
    path('patients/<str:pk>/', views.patient_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)
