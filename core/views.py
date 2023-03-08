from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import *
from .models import *

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# specialite
@csrf_exempt
def specialite_list(request):
    """
    List all code Specialites, or create a new Specialite.
    """
    if request.method == 'GET':
        specialites = Specialite.objects.all()
        serializer = SpecialiteSerializer(specialites, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SpecialiteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def specialite_detail(request, pk):
    """
    Retrieve, update or delete a code specialite.
    """
    try:
        specialite = Specialite.objects.get(pk=pk)
    except Specialite.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SpecialiteSerializer(specialite)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SpecialiteSerializer(specialite, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        specialite.delete()
        return HttpResponse(status=204)
     

# Departement
@csrf_exempt
def departement_list(request):
    """
    List all code departements, or create a new Departement.
    """
    if request.method == 'GET':
        departements = Departement.objects.all()
        serializer = DepartementSerializer(departements, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DepartementSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def departement_detail(request, pk):
    """
    Retrieve, update or delete a code departement.
    """
    try:
        departement = Departement.objects.get(pk=pk)
    except Departement.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DepartementSerializer(departement)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DepartementSerializer(departement, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        departement.delete()
        return HttpResponse(status=204)

# Ecole
@csrf_exempt
def ecole_list(request):
    """
    List all code ecoles, or create a new ecole.
    """
    if request.method == 'GET':
        ecoles = Ecole.objects.all()
        serializer = EcoleSerializer(ecoles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EcoleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def ecole_detail(request, pk):
    """
    Retrieve, update or delete a code ecole.
    """
    try:
        ecole = Ecole.objects.get(pk=pk)
    except Ecole.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EcoleSerializer(ecole)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EcoleSerializer(ecole, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ecole.delete()
        return HttpResponse(status=204)
    
# Formation
@csrf_exempt
def formation_list(request):
    """
    List all code formations, or create a new formation.
    """
    if request.method == 'GET':
        formations = Formation.objects.all()
        serializer = FormationSerializer(formations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FormationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def formation_detail(request, pk):
    """
    Retrieve, update or delete a code formation.
    """
    try:
        formation = Formation.objects.get(pk=pk)
    except Formation.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FormationSerializer(formation)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FormationSerializer(formation, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        formation.delete()
        return HttpResponse(status=204)

# Specialisations
@csrf_exempt
def specialisations_list(request):
    """
    List all code specialisationss, or create a new specialisations.
    """
    if request.method == 'GET':
        specialisationss = Specialisations.objects.all()
        serializer = SpecialisationsSerializer(specialisationss, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SpecialisationsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def specialisations_detail(request, pk):
    """
    Retrieve, update or delete a code specialisations.
    """
    try:
        specialisations = Specialisations.objects.get(pk=pk)
    except Specialisations.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SpecialisationsSerializer(specialisations)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SpecialisationsSerializer(specialisations, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        specialisations.delete()
        return HttpResponse(status=204)
    
# Clinique
@csrf_exempt
def clinique_list(request):
    """
    List all code cliniques, or create a new clinique.
    """
    if request.method == 'GET':
        cliniques = Clinique.objects.all()
        serializer = CliniqueSerializer(cliniques, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CliniqueSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def clinique_detail(request, pk):
    """
    Retrieve, update or delete a code clinique.
    """
    try:
        clinique = Clinique.objects.get(pk=pk)
    except Clinique.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CliniqueSerializer(clinique)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CliniqueSerializer(clinique, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        clinique.delete()
        return HttpResponse(status=204)


# Medcin
@csrf_exempt
def medcin_list(request):
    """
    List all code medcins, or create a new medcin.
    """
    if request.method == 'GET':
        medcins = Medcin.objects.all()
        serializer = MedcinSerializer(medcins, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MedcinSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def medcin_detail(request, pk):
    """
    Retrieve, update or delete a code medcin.
    """
    try:
        medcin = Medcin.objects.get(pk=pk)
    except Medcin.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MedcinSerializer(medcin)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MedcinSerializer(medcin, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        medcin.delete()
        return HttpResponse(status=204)

# Education
@csrf_exempt
def education_list(request):
    """
    List all code educations, or create a new education.
    """
    if request.method == 'GET':
        educations = Education.objects.all()
        serializer = EducationSerializer(educations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EducationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def education_detail(request, pk):
    """
    Retrieve, update or delete a code education.
    """
    try:
        education = Education.objects.get(pk=pk)
    except Education.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EducationSerializer(education)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EducationSerializer(education, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        education.delete()
        return HttpResponse(status=204)

# experience
@csrf_exempt
def experience_list(request):
    """
    List all code experiences, or create a new experience.
    """
    if request.method == 'GET':
        experiences = Experience.objects.all()
        serializer = ExperienceSerializer(experiences, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExperienceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def experience_detail(request, pk):
    """
    Retrieve, update or delete a code experience.
    """
    try:
        experience = Experience.objects.get(pk=pk)
    except Experience.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ExperienceSerializer(experience)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ExperienceSerializer(experience, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        experience.delete()
        return HttpResponse(status=204)


# Certificat
@csrf_exempt
def certificat_list(request):
    """
    List all code certificats, or create a new certificat.
    """
    if request.method == 'GET':
        certificats = Certificat.objects.all()
        serializer = CertificatSerializer(certificats, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CertificatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def certificat_detail(request, pk):
    """
    Retrieve, update or delete a code certificat.
    """
    try:
        certificat = Certificat.objects.get(pk=pk)
    except Certificat.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CertificatSerializer(certificat)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CertificatSerializer(certificat, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        certificat.delete()
        return HttpResponse(status=204)
    
# Galerie
@csrf_exempt
def galerie_list(request):
    """
    List all code galeries, or create a new galerie.
    """
    if request.method == 'GET':
        galeries = Galerie.objects.all()
        serializer = GalerieSerializer(galeries, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GalerieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def galerie_detail(request, pk):
    """
    Retrieve, update or delete a code galerie.
    """
    try:
        galerie = Galerie.objects.get(pk=pk)
    except Galerie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GalerieSerializer(galerie)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GalerieSerializer(galerie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        galerie.delete()
        return HttpResponse(status=204)

# Disponibilite
@csrf_exempt
def disponibilite_list(request):
    """
    List all code disponibilites, or create a new disponibilite.
    """
    if request.method == 'GET':
        disponibilites = Disponibilite.objects.all()
        serializer = DisponibiliteSerializer(disponibilites, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DisponibiliteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def disponibilite_detail(request, pk):
    """
    Retrieve, update or delete a code disponibilite.
    """
    try:
        disponibilite = Disponibilite.objects.get(pk=pk)
    except Disponibilite.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DisponibiliteSerializer(disponibilite)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DisponibiliteSerializer(disponibilite, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        disponibilite.delete()
        return HttpResponse(status=204)


# SpecialisationMedcin
@csrf_exempt
def specialisationMedcin_list(request):
    """
    List all code specialisationMedcins, or create a new specialisationMedcin.
    """
    if request.method == 'GET':
        specialisationMedcins = SpecialisationMedcin.objects.all()
        serializer = SpecialisationMedcinSerializer(specialisationMedcins, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SpecialisationMedcinSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def specialisationMedcin_detail(request, pk):
    """
    Retrieve, update or delete a code specialisationMedcin.
    """
    try:
        specialisationMedcin = SpecialisationMedcin.objects.get(pk=pk)
    except SpecialisationMedcin.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SpecialisationMedcinSerializer(specialisationMedcin)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SpecialisationMedcinSerializer(specialisationMedcin, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        specialisationMedcin.delete()
        return HttpResponse(status=204)

# Pays
@csrf_exempt
def pays_list(request):
    """
    List all code payss, or create a new pays.
    """
    if request.method == 'GET':
        payss = Pays.objects.all()
        serializer = PaysSerializer(payss, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PaysSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def pays_detail(request, pk):
    """
    Retrieve, update or delete a code pays.
    """
    try:
        pays = Pays.objects.get(pk=pk)
    except Pays.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PaysSerializer(pays)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PaysSerializer(pays, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pays.delete()
        return HttpResponse(status=204)

# Region
@csrf_exempt
def region_list(request):
    """
    List all code regions, or create a new region.
    """
    if request.method == 'GET':
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def region_detail(request, pk):
    """
    Retrieve, update or delete a code region.
    """
    try:
        region = Region.objects.get(pk=pk)
    except Region.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RegionSerializer(region)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RegionSerializer(region, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        region.delete()
        return HttpResponse(status=204)

#   Ville
@csrf_exempt
def ville_list(request):
    """
    List all code villes, or create a new ville.
    """
    if request.method == 'GET':
        villes = Ville.objects.all()
        serializer = VilleSerializer(villes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VilleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def ville_detail(request, pk):
    """
    Retrieve, update or delete a code ville.
    """
    try:
        ville = Ville.objects.get(pk=pk)
    except Ville.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VilleSerializer(ville)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VilleSerializer(ville, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ville.delete()
        return HttpResponse(status=204)

# Profession
@csrf_exempt
def profession_list(request):
    """
    List all code professions, or create a new profession.
    """
    if request.method == 'GET':
        professions = Profession.objects.all()
        serializer = ProfessionSerializer(professions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProfessionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def profession_detail(request, pk):
    """
    Retrieve, update or delete a code profession.
    """
    try:
        profession = Profession.objects.get(pk=pk)
    except Profession.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProfessionSerializer(profession)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProfessionSerializer(profession, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        profession.delete()
        return HttpResponse(status=204)

# Patient
@csrf_exempt
def patient_list(request):
    """
    List all code patients, or create a new patient.
    """
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def patient_detail(request, pk):
    """
    Retrieve, update or delete a code patient.
    """
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PatientSerializer(patient, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        patient.delete()
        return HttpResponse(status=204)

# RendezVous
@api_view(['GET', 'POST'])
def rendezVous_list(request, format=None):
    """
    List all code rendezVouss, or create a new rendezVous.
    """
    if request.method == 'GET':
        rendezVouss = RendezVous.objects.all()
        serializer = RendezVousSerializer(rendezVouss, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RendezVousSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def rendezVous_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code rendezVous.
    """
    try:
        rendezVous = RendezVous.objects.get(pk=pk)
    except RendezVous.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RendezVousSerializer(rendezVous)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RendezVousSerializer(rendezVous, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        rendezVous.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


