from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app_medcin.views.Medcin import medcin_list,medcin_detail


urlpatterns = [

    path('medcins/', views.medcin_list,name='medcin_list'),
    path('medcins/<str:pk>/', views.medcin_detail,name='medcin_detail'),

    path('educations/', views.education_list,name='education_list'),
    path('educations/<str:pk>/', views.education_detail,name='education_detail'),

    path('experiences/', views.experience_list,name='experience_list'),
    path('experiences/<str:pk>/', views.experience_detail,name='experience_detail'),

    path('certificats/', views.certificat_list,name='certificat_list'),
    path('certificats/<str:pk>/', views.certificat_detail,name='certificat_detail'),

    path('galeries/', views.galerie_list,name='galerie_list'),
    path('galeries/<str:pk>/', views.galerie_detail,name='galerie_detail'),

    path('disponibilites/', views.disponibilite_list,name='disponibilite_list'),
    path('disponibilites/<str:pk>/', views.disponibilite_detail,name='disponibilite_detail'),

    path('specialisationMedcins/', views.specialisationMedcin_list,name='specialisationMedcin_list'),
    path('specialisationMedcins/<str:pk>/', views.specialisationMedcin_detail,name='specialisationMedcin_detail'),

]
