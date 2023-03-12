from django.urls import path
from parametres.views import (
    Pays, Region, Ville, 
    Profession, Type_Piece, Piece
)

urlpatterns = [
    path('pays/', Pays.pays_list,name='pays_list'),
    path('pays/<str:pk>/', Pays.pays_detail,name='pays_detail'),

    path('regions/', Region.region_list,name='region_list'),
    path('regions/<str:pk>/', Region.region_detail,name='region_detail'),

    path('villes/', Ville.ville_list,name='ville_list'),
    path('villes/<str:pk>/', Ville.ville_detail,name='ville_detail'),

    path('professions/', Profession.profession_list,name='profession_list'),
    path('professions/<str:pk>/', Profession.profession_detail,name='profession_detail'),

    path('ajout_type_piece/', Type_Piece.ajoutType_piece, name='ajout_type_piece'),
    path('type_pieces/', Type_Piece.type_pieces, name='liste_type_pieces'),
    path('type_piece/<str:pk>/', Type_Piece.type_piece, name='type_piece'),

    path('ajout_piece/', Piece.ajoutpiece, name='ajout_piece'),
    path('pieces/', Piece.pieces, name='liste_pieces'),
    path('piece/<str:pk>/', Piece.piece, name='piece'),
]
