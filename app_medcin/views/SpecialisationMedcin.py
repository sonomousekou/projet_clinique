from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from app_medcin.serializers import SpecialisationMedcinSerializer
from app_medcin.models import SpecialisationMedcin

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