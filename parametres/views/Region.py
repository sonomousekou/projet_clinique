from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from parametres.models import Region
from parametres.serializers import RegionSerializer

# Region
@csrf_exempt
def region_list(request):
    """
    List all code regions, or create a new region.
    """
    if request.method == 'GET':
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def region_detail(request, pk):
    """
    Retrieve, update or delete a code region.
    """
    try:
        region = Region.objects.get(pk=pk)
    except Region.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RegionSerializer(region)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RegionSerializer(region, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        region.delete()
        return HttpResponse(status=204)
