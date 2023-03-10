from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from parametres.models import Ville
from parametres.serializers import VilleSerializer

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


