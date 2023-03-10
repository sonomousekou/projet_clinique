from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from parametres.serializers import EcoleSerializer
from parametres.models import Ecole

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
    
