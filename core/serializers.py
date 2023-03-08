from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

#serialisation de la classe Specialite
class SpecialiteSerializer(ModelSerializer):
    class Meta:
        model = Specialite
        fields='__all__'    

# serialisation de la classe Departement
class DepartementSerializer(ModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model=Departement
        fields=['title','description','image']  