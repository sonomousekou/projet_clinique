from django.urls import path,include
from core.views import client

urlpatterns = [
    path('',client.home),

    path('api_medcin/', include('app_medcin.urls')),
    path('api_patient/', include('app_patient.urls')),
    path('api_parametres/', include('parametres.urls')),
   
] 


