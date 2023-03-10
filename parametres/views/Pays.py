from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from parametres.models import Pays
from parametres.serializers import PaysSerializer

# Pays
@csrf_exempt
def pays_list(request):
    """
    List all code payss, or create a new pays.
    """
    if request.method == 'GET':
        payss = Pays.objects.all()
        serializer = PaysSerializer(payss, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PaysSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def pays_detail(request, pk):
    """
    Retrieve, update or delete a code pays.
    """
    try:
        pays = Pays.objects.get(pk=pk)
    except Pays.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PaysSerializer(pays)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PaysSerializer(pays, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pays.delete()
        return HttpResponse(status=204)
    