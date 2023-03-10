from rest_framework import serializers
from .models import (
	Patient,
	RendezVous
)
from parametres.serializers import (
	VilleSerializer
)

class PatientSerializer(serializers.ModelSerializer):
	"""
	Patient serializer
	Based on serializers.ModelSerializer
	"""

	photo = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

	ville = VilleSerializer(many=False, read_only=True)

	class Meta:
		model = Patient
		fields = "__all__"

class RendezVousSerializer(serializers.ModelSerializer):
	"""
	Profession serializer
	Based on serializers.ModelSerializer
	"""
	class Meta:
		model = RendezVous
		fields = "__all__"