from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from parametres.serializers import FormationSerializer
from parametres.models import Formation

   
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
    