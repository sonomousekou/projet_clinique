from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from parametres.serializers import DepartementSerializer
from parametres.models import Departement


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

