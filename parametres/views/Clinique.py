from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from parametres.serializers import CliniqueSerializer
from parametres.models import Clinique

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



