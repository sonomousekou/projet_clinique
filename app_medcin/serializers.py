from rest_framework import serializers
from .models import (
    Medcin, Education,
    Disponibilite, Experience,
    Certificat, Galerie, SpecialisationMedcin
)
from parametres.serializers import (
	SpecialiteSerializer,
	DepartementSerializer
)

class MedcinSerializer(serializers.ModelSerializer):
	"""
	Medcin serializer
	Based on serializers.ModelSerializer
	"""
	photo = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

	specialite = SpecialiteSerializer(many=False, read_only=True)
	departement = DepartementSerializer(many=False, read_only=True)
	
	class Meta:
		model = Medcin
		fields = "__all__"

class EducationSerializer(serializers.ModelSerializer):
	"""
	Education serializer
	Based on serializers.ModelSerializer
	"""
	medcin = MedcinSerializer(many=False, read_only=True)

	class Meta:
		model = Education
		fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
	"""
	Experience serializer
	Based on serializers.ModelSerializer
	"""
	medcin = MedcinSerializer(many=False, read_only=True)

	class Meta:
		model = Experience
		fields = "__all__"


class CertificatSerializer(serializers.ModelSerializer):
	"""
	Certificat serializer
	Based on serializers.ModelSerializer
	"""
	medcin = MedcinSerializer(many=False, read_only=True)

	class Meta:
		model = Certificat
		fields = "__all__"


class GalerieSerializer(serializers.ModelSerializer):
	"""
	Galerie serializer
	Based on serializers.ModelSerializer
	"""

	image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

	medcin = MedcinSerializer(many=False, read_only=True)

	class Meta:
		model = Galerie
		fields = "__all__"


class DisponibiliteSerializer(serializers.ModelSerializer):
	"""
	Disponibilite serializer
	Based on serializers.ModelSerializer
	"""
	medcin = MedcinSerializer(many=False, read_only=True)

	class Meta:
		model = Disponibilite
		fields = "__all__"


class SpecialisationMedcinSerializer(serializers.ModelSerializer):
	"""
	SpecialisationMedcin serializer
	Based on serializers.ModelSerializer
	"""
	medcin = MedcinSerializer(many=False, read_only=True)

	class Meta:
		model = SpecialisationMedcin
		fields = "__all__"

