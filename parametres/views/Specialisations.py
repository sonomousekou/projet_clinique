from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from parametres.serializers import SpecialisationsSerializer
from parametres.models import Specialisations


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
    