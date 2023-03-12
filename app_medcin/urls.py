from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app_medcin.views import (
    Medcin, Education, Experience, Certificat,
    Galerie, Disponibilite, SpecialisationMedcin

)

urlpatterns = [

    path('medcins/', Medcin.medcin_list,name='medcin_list'),
    path('medcins/<str:pk>/', Medcin.medcin_detail,name='medcin_detail'),

    path('educations/', Education.education_list,name='education_list'),
    path('educations/<str:pk>/', Education.education_detail,name='education_detail'),

    path('experiences/', Experience.experience_list,name='experience_list'),
    path('experiences/<str:pk>/', Experience.experience_detail,name='experience_detail'),

    path('certificats/', Certificat.certificat_list,name='certificat_list'),
    path('certificats/<str:pk>/', Certificat.certificat_detail,name='certificat_detail'),

    path('galeries/', Galerie.galerie_list,name='galerie_list'),
    path('galeries/<str:pk>/', Galerie.galerie_detail,name='galerie_detail'),

    path('disponibilites/', Disponibilite.disponibilite_list,name='disponibilite_list'),
    path('disponibilites/<str:pk>/', Disponibilite.disponibilite_detail,name='disponibilite_detail'),

    path('specialisationMedcins/', SpecialisationMedcin.specialisationMedcin_list,name='specialisationMedcin_list'),
    path('specialisationMedcins/<str:pk>/', SpecialisationMedcin.specialisationMedcin_detail,name='specialisationMedcin_detail'),

]
