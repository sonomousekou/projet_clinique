# Django REST Libs:
from rest_framework import serializers
# Local Libs:
from .models import RendezVous,Type_Piece, Piece,Specialite, Departement, Ecole, Formation, Specialisations, Clinique, Medcin, Education, Experience, Certificat, Galerie, Disponibilite, SpecialisationMedcin, Pays, Region, Ville, Profession, Patient

class SpecialiteSerializer(serializers.ModelSerializer):
	"""
	Specialite serializer
	Based on serializers.ModelSerializer
	"""
	
	image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

	class Meta:
		model = Specialite
		fields = "__all__"

class DepartementSerializer(serializers.ModelSerializer):
	"""
	Departement serializer
	Based on serializers.ModelSerializer
	"""

	image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

	class Meta:
		model = Departement
		fields = "__all__"


class EcoleSerializer(serializers.ModelSerializer):
	"""
	Ecole serializer
	Based on serializers.ModelSerializer
	"""
	class Meta:
		model = Ecole
		fields = "__all__"


class FormationSerializer(serializers.ModelSerializer):
	"""
	Formation serializer
	Based on serializers.ModelSerializer
	"""
	class Meta:
		model = Formation
		fields = "__all__"


class SpecialisationsSerializer(serializers.ModelSerializer):
	"""
	Specialisations serializer
	Based on serializers.ModelSerializer
	"""
	class Meta:
		model = Specialisations
		fields = "__all__"


class CliniqueSerializer(serializers.ModelSerializer):
	"""
	Clinique serializer
	Based on serializers.ModelSerializer
	"""
	class Meta:
		model = Clinique
		fields = "__all__"

class Type_PieceSerializer(serializers.ModelSerializer):
	"""
	Type_Piece serializer
	Based on serializers.ModelSerializer
	"""

	class Meta:
		model = Type_Piece
		fields = "__all__"


class PieceSerializer(serializers.ModelSerializer):
	"""
	Piece serializer
	Based on serializers.ModelSerializer
	"""
	type_piece = Type_PieceSerializer(many=False, read_only=True)

	class Meta:
		model = Piece
		fields = "__all__"


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


class PaysSerializer(serializers.ModelSerializer):
	"""
	Pays serializer
	Based on serializers.ModelSerializer
	"""
	class Meta:
		model = Pays
		fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
	"""
	Region serializer
	Based on serializers.ModelSerializer
	"""
	pays = PaysSerializer(many=False, read_only=True)


	class Meta:
		model = Region
		fields = "__all__"


class VilleSerializer(serializers.ModelSerializer):
	"""
	Ville serializer
	Based on serializers.ModelSerializer
	"""
	region = RegionSerializer(many=False, read_only=True)

	class Meta:
		model = Ville
		fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):
	"""
	Profession serializer
	Based on serializers.ModelSerializer
	"""
	class Meta:
		model = Profession
		fields = "__all__"


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