# from django.urls import path
# from core import views
# from rest_framework.urlpatterns import format_suffix_patterns
# # from core.views_parametres import Type_Piece,RendezVous,Piece
# from parametres.views_parametres import Type_Piece,Piece

# urlpatterns = [

#     path('specialites/', views.specialite_list,name='specialite_list'),
#     path('specialites/<str:pk>/', views.specialite_detail,name='specialite_detail'),

#     path('departements/', views.departement_list,name='departement_list'),
#     path('departements/<str:pk>/', views.departement_detail,name='departement_detail'),
    
#     path('ecoles/', views.ecole_list,name='ecole_list'),
#     path('ecoles/<str:pk>/', views.ecole_detail,name='ecole_detail'),

#     path('formations/', views.formation_list,name='formation_list'),
#     path('formations/<str:pk>/', views.formation_detail,name='formation_detail'),

#     path('specialisations/', views.specialisations_list,name='specialisations_list'),
#     path('specialisations/<str:pk>/', views.specialisations_detail,name='specialisations_detail'),

#     path('cliniques/', views.clinique_list,name='clinique_list'),
#     path('cliniques/<str:pk>/', views.clinique_detail,name='clinique_detail'),

#     path('medcins/', views.medcin_list,name='medcin_list'),
#     path('medcins/<str:pk>/', views.medcin_detail,name='medcin_detail'),

#     path('educations/', views.education_list,name='education_list'),
#     path('educations/<str:pk>/', views.education_detail,name='education_detail'),

#     path('experiences/', views.experience_list,name='experience_list'),
#     path('experiences/<str:pk>/', views.experience_detail,name='experience_detail'),


#     path('certificats/', views.certificat_list,name='certificat_list'),
#     path('certificats/<str:pk>/', views.certificat_detail,name='certificat_detail'),

#     path('galeries/', views.galerie_list,name='galerie_list'),
#     path('galeries/<str:pk>/', views.galerie_detail,name='galerie_detail'),

#     path('disponibilites/', views.disponibilite_list,name='disponibilite_list'),
#     path('disponibilites/<str:pk>/', views.disponibilite_detail,name='disponibilite_detail'),

#     path('specialisationMedcins/', views.specialisationMedcin_list,name='specialisationMedcin_list'),
#     path('specialisationMedcins/<str:pk>/', views.specialisationMedcin_detail,name='specialisationMedcin_detail'),

#     path('pays/', views.pays_list,name='pays_list'),
#     path('pays/<str:pk>/', views.pays_detail,name='pays_detail'),

#     path('regions/', views.region_list,name='region_list'),
#     path('regions/<str:pk>/', views.region_detail,name='region_detail'),

#     path('villes/', views.ville_list,name='ville_list'),
#     path('villes/<str:pk>/', views.ville_detail,name='ville_detail'),

#     path('professions/', views.profession_list,name='profession_list'),
#     path('professions/<str:pk>/', views.profession_detail,name='profession_detail'),

#     path('patients/', views.patient_list,name='patient_list'),
#     path('patients/<str:pk>/', views.patient_detail,name='patient_detail'),

#     # path('rendezVous/', RendezVous.rendezVous_list,name='rendezVous_list'),
#     # path('rendezVous/<str:pk>/', RendezVous.rendezVous_detail,name='rendezVous_detail'),
    
#     path('ajout_type_piece/', Type_Piece.ajoutType_piece, name='ajout_type_piece'),
#     path('type_pieces/', Type_Piece.type_pieces, name='liste_type_pieces'),
#     path('type_piece/<str:pk>/', Type_Piece.type_piece, name='type_piece'),

#     path('ajout_piece/', Piece.ajoutpiece, name='ajout_piece'),
#     path('pieces/', Piece.pieces, name='liste_pieces'),
#     path('piece/<str:pk>/', Piece.piece, name='piece'),

# ]

# # urlpatterns = format_suffix_patterns(urlpatterns)
