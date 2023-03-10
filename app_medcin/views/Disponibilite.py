from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from app_medcin.serializers import DisponibiliteSerializer
from app_medcin.models import Disponibilite

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
