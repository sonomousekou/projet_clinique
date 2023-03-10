from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from app_medcin.serializers import CertificatSerializer
from app_medcin.models import Certificat


# Certificat
@csrf_exempt
def certificat_list(request):
    """
    List all code certificats, or create a new certificat.
    """
    if request.method == 'GET':
        certificats = Certificat.objects.all()
        serializer = CertificatSerializer(certificats, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CertificatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def certificat_detail(request, pk):
    """
    Retrieve, update or delete a code certificat.
    """
    try:
        certificat = Certificat.objects.get(pk=pk)
    except Certificat.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CertificatSerializer(certificat)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CertificatSerializer(certificat, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        certificat.delete()
        return HttpResponse(status=204)
    