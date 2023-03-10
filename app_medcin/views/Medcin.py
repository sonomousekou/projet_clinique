from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from app_medcin.serializers import MedcinSerializer
from app_medcin.models import Medcin

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