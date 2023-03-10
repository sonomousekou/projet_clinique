from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from app_medcin.serializers import GalerieSerializer
from app_medcin.models import Galerie

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

