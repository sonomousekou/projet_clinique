from rest_framework import serializers
from .models import(
            Type_Piece,Piece,
            Departement, Specialisations, Specialite, 
            Pays , Ville, Region,
            Clinique, Formation, Profession, Ecole
) 

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

class SpecialisationsSerializer(serializers.ModelSerializer):
	"""
	Specialisations serializer
	Based on serializers.ModelSerializer
	"""
	class Meta:
		model = Specialisations
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

class CliniqueSerializer(serializers.ModelSerializer):
	"""
	Clinique serializer
	Based on serializers.ModelSerializer
	"""
	class Meta:
		model = Clinique
		fields = "__all__"
		
class ProfessionSerializer(serializers.ModelSerializer):
	"""
	Profession serializer
	Based on serializers.ModelSerializer
	"""
	class Meta:
		model = Profession
		fields = "__all__"

