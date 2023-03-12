from django.urls import path
from app_patient.views import (
    Patient, RendezVous
)

urlpatterns = [
    path('patients/', Patient.patient_list,name='patient_list'),
    path('patients/<str:pk>/', Patient.patient_detail,name='patient_detail'),

    path('rendezVous/', RendezVous.rendezVous_list,name='rendezVous_list'),
    path('rendezVous/<str:pk>/', RendezVous.rendezVous_detail,name='rendezVous_detail'),
    
]
